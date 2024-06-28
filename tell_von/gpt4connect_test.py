import unittest
from unittest.mock import patch
from tell_von.gpt4connect import ask_gpt4

class TestGpt4Connect(unittest.TestCase):

    @patch('gpt4connect.OpenAI')
    def test_ask_gpt4(self, mock_openai):
        # Mock the OpenAI client
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value.choices[0].message.content = "Response from GPT-4"

        # Test case 1: Prompt with system message
        prompt_text = "How do I output all files in a directory using Python?"
        system_prompt = "System message"
        expected_response = "You can use the `os` and `glob` modules i[606 chars]r()`"
        response = ask_gpt4(prompt_text, system_prompt)
        self.assertEqual(response, expected_response)

        # Test case 2: Prompt without system message
        prompt_text = "Who won the world series in 2020?"
        expected_response = "The 2020 World Series was played between the Los Angeles Dodgers and the Tampa Bay Rays at Globe Life Field in Arlington, Texas."
        response = ask_gpt4(prompt_text)
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()