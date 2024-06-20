# ChatBot with GUI

## Project Overview

### Team Members
- Ana Kreidenko
- Nato Tsertsvadze
- Natia Pruidze
- Nika Gubeladze

### Problem Statement
In the contemporary digital landscape, efficient and intelligent chatbots are crucial for enhancing user experience and providing seamless customer support. However, building a chatbot capable of understanding natural language, generating contextually relevant responses, and adapting to new information presents significant challenges.

This project aims to address these challenges by developing a sophisticated chatbot solution utilizing machine learning (ML) and natural language processing (NLP) techniques. The primary objectives include:

1. **Effective Communication**: Accurately interpreting user queries and responding with relevant information in human-like conversation patterns.
   
2. **Dynamic Learning**: Implementing mechanisms for the chatbot to learn from user interactions and adapt its responses over time, ensuring continuous improvement.

3. **Context Management**: Facilitating multi-turn dialogues by maintaining context across interactions, thereby enabling coherent and personalized conversations.

### Objectives
1. **Understand User Queries**: Accurately classify user inputs into predefined intents (categories).
   
2. **Generate Appropriate Responses**: Based on classified intents, provide relevant and contextually appropriate responses to users.

3. **Maintain Context**: Handle multi-turn conversations effectively by retaining context across interactions.

4. **Training and Adaptation**: Enable users to add new intents, patterns, and responses, allowing the chatbot to dynamically learn and improve.

### Expected Outcomes
- **Accurate Classification**: The chatbot will classify user queries into predefined intents with high accuracy using ML models and NLP techniques.
  
- **Appropriate Responses**: It will generate contextually relevant responses for each classified intent, enhancing user interaction and satisfaction.
  
- **Contextual Understanding**: The chatbot will maintain conversational context, facilitating seamless multi-turn dialogues.
  
- **Dynamic Training**: Users can enrich the chatbot's knowledge base by adding new training data through a user-friendly interface, ensuring continuous improvement.

## Technical Details

### AI/ML Techniques Used

#### Natural Language Processing (NLP)
NLP techniques are employed extensively to preprocess user inputs and enable the chatbot to understand and respond appropriately:
- **Tokenization**: Break down user input into individual words or tokens using `word_tokenize` from NLTK.
  
- **Lemmatization**: Reduce words to their base or root form using `WordNetLemmatizer` from NLTK, ensuring consistency in data representation.
  
- **Stop Words Removal and Filtering**: Eliminate non-essential words and symbols to focus on meaningful content.

#### Machine Learning (ML) and Neural Networks
The core ML technique utilized is a neural network model built with TensorFlow Keras:
- **Model Architecture**: Includes input layer, hidden layers with dropout for regularization, and output layer with softmax activation for classification.
  
- **Training Process**: Trains the model on labeled data to optimize weights and minimize prediction errors.
  
- **Vectorization**: Converts words into numerical representations (vectors) using techniques like `pad_sequences` and `CountVectorizer`.

### Optimization Techniques
Optimization techniques such as Stochastic Gradient Descent (SGD) with learning rate decay and momentum are employed to enhance model training efficiency and accuracy.

## Project Structure
- **chatbot_gui.py**: Provides a graphical user interface (GUI) for user interaction with the chatbot and training data management.
  
- **training.py**: Handles the training of the chatbot using a neural network model, preparing it to classify intents and generate responses based on user queries.
  
- **testing.py**: Implements the chatbot's response mechanism, utilizing the trained model to classify intents and generate appropriate responses.

## 5. Installation and Setup

To run the ChatBot application:

1. Install Python (if not already installed) from [python.org](https://www.python.org/).

2. Install required Python packages:
    ```bash
    pip install numpy nltk tensorflow keras
    ```

3. Run the application:
    ```bash
    python chatbot_GUI.py
    ```



## Usage
1. **Running the ChatBot**: Execute `chatbot_gui.py` to launch the graphical interface.
   
2. **Interacting with the ChatBot**: Enter queries in the chat window to receive responses from the chatbot.
   
3. **Training the ChatBot**: Use the training interface to add new intents, patterns, and responses to enhance the chatbot's capabilities.

## Benefits
- **Practical Application of AI**: Demonstrates the application of ML and NLP techniques in building interactive systems.
  
- **Hands-on Learning**: Provides an example of leveraging machine learning for NLP, applicable across various use cases.
