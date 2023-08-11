# text-to-speech
Turn a pdf file into an audiobook.

# Update Aug 10, 2023
The textcompile.py script works fine, and it's imported into main.py. The associated lines in main.py are commented out while I test the program using a hard-coded, simple line of text. Other than that...

The code successfully sends text to Amazon Web Services where Amazon Polly synthesized the text into speech. The resulting .mp3 file is successfully stored into the S3 storage system. That's the end of the good news. It seems a straightforward thing to download a file from S3, given proper permissions. This is not the case, however. I have tried all kinds of things to get it to work - including unblocking all public access and granting full permissions to all resources - to no avail. I always get this error:

botocore.exceptions.ClientError: An error occurred (403) when calling the HeadObject operation: Forbidden

I can log into AWS and manually download it, but that defeats half the purpose of the project. I'll keep looking for an answer.
