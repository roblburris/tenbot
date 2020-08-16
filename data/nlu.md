## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks

## intent:bye
- goodbye
- goodnight
- good bye
- good night
- see ya
- toodle-oo
- bye bye
- gotta go
- farewell

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers

## intent: faq/ask_channels
- What channels of communication does rasa support?
- what channels do you support?
- what chat channels does rasa uses
- channels supported by Rasa
- which messaging channels does rasa support?

## intent: faq/ask_languages
- what language does rasa support?
- which language do you support?
- which languages supports rasa
- can I use rasa also for another laguage?
- languages supported

## intent: faq/ask_rasax
- I want information about rasa x
- i want to learn more about Rasa X
- what is rasa x?
- Can you tell me about rasa x?
- Tell me about rasa x
- tell me what is rasa x

## intent:contact_sales
- I wanna talk to your sales people.
- I want to talk to your sales people
- I want to speak with sales
- Sales
- Please schedule a sales call
- Please connect me to someone from sales
- I want to get in touch with your sales guys
- I would like to talk to someone from your sales team
- sales please

## regex:patient_email
- \<(.*)@(.*).com\>

## regex:patient_reason
- .*

## lookup:patient_name
training-data/names.txt


## intent:inform
- My name is [Peter Parker](patient_name)
- name [Jian Yang](patient_name)
- [Tyler Blevins](patient_name)
- I'm [Brad Pitt](patient_name)
- my phone num is [4250691213](patient_number]
- My phone number [423-341-8903](patient_number]
- number is [(425)-900-9142](patient_number)
- [415 672 4623](patient_number)
- My email is [john.doe@gmail.com](patient_email)
- Email [jakcks@hotmail.com](patient_email)
- [bachmann-erlich@yahoo.com](patient_email)
- [rich-ehndricsk@outlook.com](patient_email)
- I want to see the doctor because [I have a sore throat](patient_reason)
- [need more medication](patient_reason)
- I'm interested in discussing [new treatment options](patient_reason)
- [I think I have COVID-19](patient_reason)


## intent:explain
- why
- why is that
- why do you need it
- why do you need to know that?
- could you explain why you need it?

## intent:out_of_scope
- I want to order food
- What is 2 + 2?
- Who’s the US President?
- I need a job
