from gpt4all import GPT4All

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

print("-------------------------------------")
print("Loading the model. please wait...")
print("============================================================")
print("Welcome to the Offline AI assistant!")
print("============================================================")
print("Created by: Corvus Codex")
print("Github: https://github.com/CorvusCodex/")
print("Licence : MIT License")
print("Support my work:")
print("BTC: bc1q7wth254atug2p4v9j3krk9kauc0ehys2u8tgg3")
print("ETH & BNB: 0x68B6D33Ad1A3e0aFaDA60d6ADf8594601BE492F0")
print("Buy me a coffee: https://www.buymeacoffee.com/CorvusCodex")
print("============================================================")

while True:
    # Ask for user input
    user_input = input("Please enter a prompt: ")

    if user_input.lower() == 'quit':
        break

    # Print a message to indicate that the model is generating a response
    print("Generating response...")

    # Generate output based on the user input
    output = model.generate(user_input, max_tokens = 300)

    # Print the output
    print(output)

    # Print a separator
    print("-------------------------------------")
