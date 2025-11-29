#!/usr/bin/env python3
import re
import sys

def remove_newsletter_context(file_path):
    """Remove newsletter contextInfo blocks from JavaScript files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match contextInfo blocks with newsletter info
    # This matches the entire contextInfo object that contains forwardedNewsletterMessageInfo
    pattern = r',\s*contextInfo:\s*\{\s*forwardingScore:\s*\d+,\s*isForwarded:\s*true,\s*forwardedNewsletterMessageInfo:\s*\{\s*newsletterJid:\s*[\'"]120363161513685998@newsletter[\'"]\s*,\s*newsletterName:\s*[\'"][^\'"]*[\'"]\s*,\s*serverMessageId:\s*-1\s*\}\s*\}'
    
    # Remove the pattern
    cleaned_content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"Cleaned: {file_path}")

if __name__ == '__main__':
    for file_path in sys.argv[1:]:
        try:
            remove_newsletter_context(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
