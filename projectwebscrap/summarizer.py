from transformers import BartTokenizer, BartForConditionalGeneration

class WebSummarizer:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    def summarize(self, text, max_length=150):
        try:
            inputs = self.tokenizer(
                text,
                max_length=1024,
                truncation=True,
                return_tensors="pt"
            )

            summary_ids = self.model.generate(
                inputs["input_ids"],
                num_beams=4,
                max_length=max_length,
                early_stopping=True
            )

            summary = self.tokenizer.decode(
                summary_ids[0],
                skip_special_tokens=True
            )

            return summary

        except Exception as e:
            print(f"[ERROR] Summarization failed: {e}")
            return "Could not summarize the content."
