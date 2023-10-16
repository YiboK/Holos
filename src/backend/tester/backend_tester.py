from ..util import chatgpt


def test():
    result = chatgpt.generateSchedule("Say hello")
    assert "Hello" in result or "hello" in result

    sentence = """
    I would like to study computer science. 
    I currently have no knowledge in this area. 
    There are some specific terms I would like to learn, such as binary tree. 
    I would like the study program to include no assignments, and I can dedicate 12 weeks to completing it. 
    """
    result = chatgpt.generateSchedule(sentence)
    assert "binary tree" in result or "Binary tree" in result

if __name__ == "__main__":
    try:
        test()
        print("Pass all tests!")
    except AssertionError as e:
        print("Assertion failed:", e)