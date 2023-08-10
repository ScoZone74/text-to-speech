import boto3
import time
from pathlib import Path
import os

from textcompile import CompileText

# compiler = CompileText()
# doc = compiler.get_text("Exist.pdf")
doc = "This is a sample text to be synthesized and stored in my brand new S3 bucket!"
# ##### CREATE AUDIO FILE ##### #
def speech_synth(text):
    aws_mag_con = boto3.Session(profile_name="ScoZone_2")
    polly_client = aws_mag_con.client(service_name="polly", region_name="us-east-1")
    response = polly_client.start_speech_synthesis_task(VoiceId="Joanna",
                                                        OutputS3BucketName="audio-books-bucket",
                                                        OutputS3KeyPrefix="vsynth",
                                                        OutputFormat="mp3",
                                                        Text=doc,
                                                        Engine="neural")

    taskId = response["SynthesisTask"]["TaskId"]
    print(f"Task ID: {taskId}")
    task_status = polly_client.get_speech_synthesis_task(TaskId=taskId)
    print(f"Status: {task_status}")
    return taskId

# ##### RETRIEVE AUDIO FILE ##### #
task_id = speech_synth(doc)
obj_key = "vsynth." + task_id + ".mp3"

time.sleep(20) # Allow time for audiofile to be created and stored in s3.

output_path = os.path.join(r"C:\Users\scozo\OneDrive\Desktop\AudioPhile", obj_key)

def retrieve_audiofile(key, path):
    resource = boto3.resource("s3")
    my_bucket = resource.Bucket("audio-books-bucket")
    my_bucket.download_file(key, path)

retrieve_audiofile(obj_key, output_path)
