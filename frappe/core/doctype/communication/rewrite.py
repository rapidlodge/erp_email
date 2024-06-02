import frappe
from openai import OpenAI

@frappe.whitelist()
def rewrite_ai(content,tone):
    #! Here content parameter pass from views-communication.js, and data from a text editor field
    #! Which datatype I suppose, html, so we convert html data to string
    #! pip install beautifulsoup
    #! I tried to check if the parameter was empty or not, but it did not work.
    #! So, I Convert the datatype to string, to check if the parameter is empty or not.
    from bs4 import BeautifulSoup # You might need to install the 'beautifulsoup4' package
    # Assuming 'content' contains the HTML content from the text editor field
    html_content = content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the plain text from the HTML content
    plain_text = soup.get_text()
    #! To check if the parameter is empty or not.
    if plain_text:
    #! Check if the tone is selected or not
    #! If Selected Then the program will rewrite
        if tone:
            #? Declare the prompt empty, will assigned value here based on the used select tone
            prompt = ""
            #? Based on the user select tone, prompt will assign
            if tone == "Human Like":
                prompt = """Imagine you are a content generator. To write effective content both
                "perplexity" and "burstiness" are
                important. Perplexity assesses text complexity and burstiness
                evaluates sentence variation. People often write with
                a mix of long and short sentences, while machine generated
                sentences tend to be uniform. I will provide you with an
                Email and ask you to rewrite it when composing the content you need
                to ensure a suitable balance of both
                perplexity and burstiness.  Do not add subject. """
            elif tone == "More Persuasive":
                prompt = "Rewrite my email with powerful, convincing language that will leave my readers no choice but to take action.  Do not add subject"
            elif tone == "More Informative":
                prompt = "Rewrite my email with rich, informative details that will leave myreaders feeling educated and informed.  Do not add subject"
            elif tone == "More Descriptive":
                prompt = "Rewrite my email with evocative, descriptive language that paints avivid and unforgettable picture in my readers' minds.  Do not add subject"
            elif tone == "More Humorous":
                prompt = "Rewrite my email with clever, comedic touches that will leave my readers laughing and entertained.  Do not add subject"
            elif tone == "Urgent":
                prompt = "Rewrite my email with urgent, action-oriented language that will inspire my readers to take immediate action.  Do not add subject"
            elif tone == "More Emphatic":
                prompt = "Rewrite my email with emphasis on the emotions and feelings of the characters or subjects I'm writing about, making the reader feel and connect with the story more.  Do not add subject"
            elif tone == "More Concise":
                prompt = "Rewrite my email using more concise and to-the-point language, making it more direct and easy to understand for my readers. Do not add subject"
                #! Final Prompt Which will be pass to OPENAI
            command = f"{prompt}\n\n{content} "
                #! Fro Error Handling, use try, expect
            try:
                client = OpenAI(api_key="")
                # openai.api_key = "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"
                response = client.completions.create(
                    # model="text-davinci-003",
                    model = "gpt-3.5-turbo-instruct",
                    prompt=command,
                    temperature=0.89,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                result = response.choices[0].text
                new_result = result.replace("\n", "<br>")
                # print(new_result)
                return new_result
            except Exception as e:
                frappe.msgprint(e)
                # pass
        else:
            frappe.msgprint("For Rewrite You Have to Select Tone.")

    else:
        frappe.msgprint("No content in the message filed")



# rewrite_ai(content="My Name is Shahadat.I want express myself as an engineer",tone="More Concise")


@frappe.whitelist()
def generate_reply(content, tone):
    #! This Function is for generate a reply mail, based on the received mail
    # frappe.msgprint("I am From, generate_reply,emai.py")
    print("")
    print("")
    print(content)
    print("")
    print("")
    if tone:
        #? Declare the prompt empty, will assigned value here based on the used selected tone
        prompt = ""
        #? Based on the user select tone, prompt will assign
        if tone == "Human Like":
            prompt = """Imagine you are a content generator. To write effective content both
            "perplexity" and "burstiness" are important. Perplexity assesses
            text complexity and burstiness evaluates sentence variation. People
            often write with a mix of long and short sentences, while machine
            generated sentences tend to be uniform. I will provide you with an
            Email and ask you to Generate a reply mail based my email when composing
            the content you need to ensure a suitable balance of both perplexity and
            burstiness."""
        elif tone == "More Persuasive":
            prompt = "Generate a reply mail based my email with powerful, convincing language that will leave my readers no choice but to take action."
        elif tone == "More Informative":
            prompt = "Generate a reply mail based on my email with rich, informative details that will leave my readers feeling educated and informed."
        elif tone == "More Descriptive":
            prompt = "Generate a reply mail based on my email with evocative, descriptive language that paints a vivid and unforgettable picture in my readers' minds."
        elif tone == "More Humorous":
            prompt = "Generate a reply mail based on my email with clever, comedic touches that will leave my readers laughing and entertained."
        elif tone == "Urgent":
            prompt = "Generate a reply mail based on my email with urgent, action-oriented language that will inspire my readers to take immediate action."
        elif tone == "More Emphatic":
            prompt = "Generate a reply mail based on my email with emphasis on the emotions and feelings of the characters or subjects I'm writing about, making the reader feels and connect with the story more."
        elif tone == "More Concise":
            prompt = "Generate a reply mail based on my email using more concise and to-the-point language, making it more direct and easy to understand for my readers."
        command = f"{prompt}\n\n{content} "
                #! Fro Error Handling, use try, expect
        try:
            client = OpenAI(api_key="")
                # openai.api_key = "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"
            response = client.completions.create(
                    # model="text-davinci-003",
                    model = "gpt-3.5-turbo-instruct",
                    prompt=command,
                    temperature=0.89,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
            result = response.choices[0].text
            new_result = result.replace("\n", "<br>")
            print("")
            print("")
            print(new_result)
            print("")
            print("")
            return new_result
        except Exception as e:
            frappe.msgprint(e)
            # pass
    else:
        frappe.msgprint("For Rewrite You Have to Select Tone.")