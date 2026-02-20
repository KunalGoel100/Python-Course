from twilio.rest import Client

Actual_SID = "ACb890420c4e9555ef114ae4d3970a7b43"
Actual_Token = "1e024c06e51adb1a6c08e52177835f32"
Actual_Number = "whatsapp:+14155238886"

client = Client(Actual_SID,Actual_Token)
message = client.messages.create(
    body = "Hi this is automated text",
    from_ = Actual_Number,
    to = "whatsapp:+919654291639"
)
print(message.status)