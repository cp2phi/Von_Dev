import unittest
#from unittest.mock import patch
from tell_von.gpt4connect import ask_gpt4,get_client

class TestGpt4Connect(unittest.TestCase):

 #   @patch('gpt4connect.OpenAI')
    def test_ask_gpt4_1(self): #, mock_openai):
        # Mock the OpenAI client
        #mock_client = mock_openai.return_value
        #mock_client.chat.completions.create.return_value.choices[0].message.content = "Response from GPT-4"

        # Test case 1: Prompt with system message
        prompt_text = "How do I output all files in a directory using Python?"
        system_prompt = "You are an expert on filesystem programming"
        response = ask_gpt4(prompt_text, system_prompt)
        print(f"Test 1 Response: {response}")
        expected_response = "os"
        self.assertIn(expected_response, response)
        expected_response = "module"
        self.assertIn(expected_response, response)


    def test_ask_gpt4_2(self):#, mock_openai):
        # Mock the OpenAI client
        #mock_client = mock_openai.return_value
        #mock_client.chat.completions.create.return_value.choices[0].message.content = "Response from GPT-4"

        # Test case 2: Prompt without system message
        prompt_text = "Who won the world series in 2020?"
        expected_response = "Dodgers"
        response = ask_gpt4(prompt_text)
        print(f"Test 2 Response: {response}")
        self.assertIn(expected_response,response )

    def test_get_client_1(self):#, mock_openai):
        response = get_client().chat.completions.create(
            model="llama3",
            messages=[ # derived from ollama documentation 
                {"role": "system", "content": "You are a auestion answering assistant."},
                {"role": "user", "content": "Who won the US baseball world series in 2020?"},
                {"role": "assistant", "content": "The LA Dodgers won in 2020."},
                {"role": "user", "content": "Where was that game played?"}
            ]
        )
        result = response.choices[0].message.content
        print("get_client based response:", result)
        self.assertIn("Arlington", result)

if __name__ == '__main__':
    unittest.main()