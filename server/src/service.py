from cassandra.cluster import Cluster
import chatgpt
import pandas as pd

class CassDB():
    def __init__(self):
        #connect to the database
        try:
            cluster = Cluster(['server-db-1', 'server-db-2', 'server-db-3'])
            self.session = cluster.connect()
        except Exception as e:
            print("initializing failing!!!!!!")
            print(e)
        self.cache = {}
        self.session.execute("drop keyspace if exists user")
        
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS user
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3}
        """)

        # create stations table
        self.session.execute("""
            CREATE TABLE IF NOT EXISTS user.preference (
                subject text,
                topic text,
                id text,
                duration int,
                PRIMARY KEY (subject, topic,id)
            )WITH CLUSTERING ORDER BY (topic ASC)
        """)

        self.insert_statement = self.session.prepare("""
            INSERT INTO user.preference
            (subject,topic,id,duration)
            VALUES
            (?,?,?,?)
            """)
        
        self.getCount = self.session.prepare("""
        SELECT subject,count(*) as cnt FROM user.preference GROUP BY subject
        """)
        
        self.getTopicCount = self.session.prepare("""SELECT topic,count(*) as cnt FROM user.preference where subject = (?) GROUP BY topic""")
        
               
    def insert(self,subject,topic,id, duration):
        try:
            if subject in self.cache:
                subject = self.cache[subject]
            else:
                self.cache[subject] = chatgpt.generateSchedule(subject).lower()
                subject = self.cache[subject]
                
            if topic in self.cache:
                topic = self.cache[topic]
            else:
                self.cache[topic] = chatgpt.generateSchedule(topic).lower()
                topic = self.cache[topic]        
            #topic = chatgpt.generateSchedule(topic).lower()
            self.session.execute(self.insert_statement, (subject,topic,id,duration))
        except ValueError as e:
            print(e)
            ret = str(e)
        except Exception as e:
            print(3, e)
        return 
    
    def getTopNTopicsBySubject(self,n,subject):
        try:
            df=pd.DataFrame(self.session.execute(self.getTopicCount, (subject,)))
            dc = {row['topic']: row['cnt'] for _, row in df.iterrows()}
            top_n = sorted(dc, key=dc.get, reverse=True)[:n]
            top_n_dict = {key: dc[key] for key in top_n}
            return top_n_dict
        except Exception as e:
            print(e)
        return None
    
    def getTopNSubjects(self,n):
        try:
            self.showDatabase()
            df=pd.DataFrame(self.session.execute(self.getCount))
            for _, row in df.iterrows():
                print(row)
            dc = {row['subject']: row['cnt'] for _, row in df.iterrows()}
            print("dc",dc)
            top_n = sorted(dc, key=dc.get, reverse=True)[:n]
            top_n_dict = {key: dc[key] for key in top_n}
            print(top_n_dict)
            return top_n_dict
        except Exception as e:
            print(e)
        return None
    
    def showDatabase(self):
        print(pd.DataFrame(self.session.execute("select * from user.preference")))
        return
    

    