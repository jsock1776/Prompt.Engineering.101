import re
import spacy

# Load spaCy model once for the NLP-based method
nlp = spacy.load("en_core_web_sm")

class LLMPostProcessor:
    def __init__(self):
        # Add any initialization parameters here if needed
        pass

    def remove_intro_statement(self, text):
        """Remove introductory statements based on both regex and NLP."""
        # Step 1: Basic regex to catch common phrases
        text = re.sub(r"^(Sure|Certainly|Here (are|is)|Let me|Allow me|In summary|To answer your question)\s*[:,\-]\s*", "", text, flags=re.IGNORECASE)
        
        # Step 2: NLP-based sentence parsing for low-content first sentences
        doc = nlp(text)
        if doc.sents:
            first_sentence = next(doc.sents)
            # Check for low-content first sentence
            if any(keyword in first_sentence.text.lower() for keyword in ["here", "sure", "certainly", "let me", "allow me", "in summary"]):
                text = text.replace(first_sentence.text, "").strip()
        
        return text.strip()

    def standardize_bullet_points(self, text):
        """Standardize bullet points to a consistent format."""
        text = re.sub(r'(\n|^)\s*[-*•]\s+', '\n• ', text)  # Convert all bullet styles to •
        return text.strip()

    def remove_bold_markers(self, text):
        """Remove bold markers such as ** or __."""
        return re.sub(r'\*\*(.*?)\*\*', r'\1', text)

    def normalize_numbered_lists(self, text):
        """Ensure numbered lists are consistently formatted."""
        return re.sub(r'\n?(\d+)\.\s+', r'\n\n\1. ', text)

    def clean_excessive_spacing(self, text):
        """Remove excessive newlines and standardize spacing between sections."""
        return re.sub(r'\n{2,}', '\n\n', text).strip()

    def process(self, text, remove_intro=True, bullet_standardization=True, bold_removal=True, list_normalization=True, spacing_cleanup=True):
        """
        Apply selected post-processing steps to the text.
        
        Parameters:
            - text (str): The input text to process.
            - remove_intro (bool): Whether to remove introductory statements.
            - bullet_standardization (bool): Whether to standardize bullet points.
            - bold_removal (bool): Whether to remove bold formatting.
            - list_normalization (bool): Whether to normalize numbered lists.
            - spacing_cleanup (bool): Whether to clean up excessive spacing.
        """
        if remove_intro:
            text = self.remove_intro_statement(text)
        if bullet_standardization:
            text = self.standardize_bullet_points(text)
        if bold_removal:
            text = self.remove_bold_markers(text)
        if list_normalization:
            text = self.normalize_numbered_lists(text)
        if spacing_cleanup:
            text = self.clean_excessive_spacing(text)
        
        return text

# Instantiate the processor
post_processor = LLMPostProcessor()
