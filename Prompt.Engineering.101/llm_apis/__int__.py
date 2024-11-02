# Import each API function
from .gpt4_api import call_gpt4
from .claude_api import call_claude
from .gemini_api import call_gemini

# Expose them at the package level
__all__ = ["call_gpt4", "call_claude", "call_gemini"]
