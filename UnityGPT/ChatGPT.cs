using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

namespace OpenAI
{
    public class ChatGPT : MonoBehaviour
    {
        [SerializeField] private InputField inputField;
        [SerializeField] private Button button;
        [SerializeField] private ScrollRect scroll;
        
        [SerializeField] private RectTransform sent;
        [SerializeField] private RectTransform received;

        private float height;
        private OpenAIApi openai = new OpenAIApi();

        private List<ChatMessage> messages = new List<ChatMessage>();
        private string prompt = @" I want you to play an academic advisor who want to design a study plan based on the student¡¯s requirements that meets their needs and background.You need to learn their requirements by asking the following questions one by one: 

        1.	What field of study would you like to learn this time?
        2.	Do you have any knowledge of the field of study before?
        If yes: What topic have you learned before? Do you want to include a review session about those topics?
        3.	What specific topic would you like to learn?
        4.	Do you want to include some assignments?
        If yes: which difficulty would you like to start with? (Easy, Medium, Hard)
        5.	How long do you plan to complete this study? (e.g., Hours, Weeks, Months)

        Once you have received the answers from your students, you will need to complete the following sentences as a summary based on the answers:

        ¡°I would like to study [subject/topic]. I currently have (some/no) knowledge in this area (including [terms]). There are some specific terms I would like to learn, such as [terms]. I would like the study program to include (no/some [difficulty level]) assignments, and I can dedicate [learning duration] to completing it.¡±

        After completing the summary, you will use the summary as a prompt to generate a study plan and ask the student if they are satisfied with the generated plan and if they need to make any adjustments.

        Don't break character. Don't ever mention that you are an AI model.
        ";

        private void Start()
        {
            SendReply();
            button.onClick.AddListener(SendReply);
        }

        private void AppendMessage(ChatMessage message)
        {
            scroll.content.SetSizeWithCurrentAnchors(RectTransform.Axis.Vertical, 0);

            var item = Instantiate(message.Role == "user" ? sent : received, scroll.content);
            item.GetChild(0).GetChild(0).GetComponent<Text>().text = message.Content;
            item.anchoredPosition = new Vector2(0, -height);
            LayoutRebuilder.ForceRebuildLayoutImmediate(item);
            height += item.sizeDelta.y;
            scroll.content.SetSizeWithCurrentAnchors(RectTransform.Axis.Vertical, height);
            scroll.verticalNormalizedPosition = 0;
        }

        private async void SendReply()
        {
            var newMessage = new ChatMessage()
            {
                Role = "user",
                Content = inputField.text
            };

            if (messages.Count != 0) AppendMessage(newMessage);

            if (messages.Count == 0) newMessage.Content = prompt + "\n" + inputField.text; 
            
            messages.Add(newMessage);
            
            button.enabled = false;
            inputField.text = "";
            inputField.enabled = false;
            
            // Complete the instruction
            var completionResponse = await openai.CreateChatCompletion(new CreateChatCompletionRequest()
            {
                Model = "gpt-3.5-turbo",
                Messages = messages
            });

            if (completionResponse.Choices != null && completionResponse.Choices.Count > 0)
            {
                var message = completionResponse.Choices[0].Message;
                message.Content = message.Content.Trim();
                
                messages.Add(message);
                AppendMessage(message);
            }
            else
            {
                Debug.LogWarning("No text was generated from this prompt.");
            }

            button.enabled = true;
            inputField.enabled = true;
        }
    }
}
