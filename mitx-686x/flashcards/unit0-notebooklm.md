# ML Flashcards

## Card 1

**Q:** Term: Machine Learning

**A:** Definition: A discipline focused on designing and applying computer programs that learn to solve tasks from experience. Example: An algorithm that improves its ability to identify spam emails after being shown thousands of examples.

---

## Card 2

**Q:** What are the three primary reasons or goals for a machine to learn from data?

**A:** To model/understand how things work, to predict future outcomes, and to control systems toward a desired configuration.

---

## Card 3

**Q:** Term: Training Set ($S_N$)

**A:** Definition: A collection of $n$ pairs, each consisting of a feature vector and its associated label, used to train a learning algorithm. Example: A set of four movies where each has a list of attributes and a rating of $+1$ or $-1$.

---

## Card 4

**Q:** Term: Feature Vector ($x$)

**A:** Definition: A representation of an example as a point or vector in a multi-dimensional space that a computer can interpret. Example: A binary vector $(1, 0, 1)$ representing that a movie is 'Action', not 'Comedy', and is 'Science Fiction'.

---

## Card 5

**Q:** Term: Label ($y$)

**A:** Definition: The target output or category associated with a specific training example in supervised learning. Example: Assigning a value of $-1$ to denote that a user disliked a specific film.

---

## Card 6

**Q:** Term: Classifier

**A:** Definition: A mapping function that takes a feature vector from a defined space and assigns it a corresponding label. Example: A function that processes an image's pixel data and outputs the category 'mushroom'.

---

## Card 7

**Q:** Term: Linear Classifier

**A:** Definition: A classifier that assigns labels by dividing the feature space into two halves using a linear boundary. Example: A straight line on a 2D graph separating positive training examples from negative ones.

---

## Card 8

**Q:** How does a linear classifier determine the label of a new point in space?

**A:** It determines which side of the linear boundary (hyperplane) the point falls on and assigns the corresponding label.

---

## Card 9

**Q:** What is the purpose of the indicator function, denoted by double brackets $[[ ... ]]$, in machine learning error calculations?

**A:** It evaluates a logical statement, returning $1$ if the statement is true (an error occurred) and $0$ if it is false.

---

## Card 10

**Q:** Formula: Training Error ($E_n$) for a classifier $h$

**A:** $E_n(h) = \frac{1}{n} \sum_{i=1}^n [[h(x^{(i)}) \ne y^{(i)}]]$, where $n$ is the number of training examples and $h(x^{(i)})$ is the predicted label.

---

## Card 11

**Q:** Under what condition is a classifier's training error considered 'chance behaviour' in a binary classification task?

**A:** When the error rate is exactly $0.5$ (or $1/2$), indicating it performs no better than flipping a coin.

---

## Card 12

**Q:** Term: Generalisation

**A:** Definition: The ability of a machine learning model to accurately predict labels for new, unseen test examples. Example: A movie recommender correctly identifying that a user will like a future film based on their past ratings.

---

## Card 13

**Q:** What is the primary difference between a training set and a test set?

**A:** The training set is used to illustrate the task and select a classifier, while the test set contains unknown examples used to evaluate real-world performance.

---

## Card 14

**Q:** How does the complexity of the 'hypothesis class' (set of possible classifiers) typically affect generalisation?

**A:** Increasing the complexity of the classifier set often leads to poorer generalisation as the models may overfit the training data.

---

## Card 15

**Q:** Pitfall: What is the risk of allowing a classifier to 'wrap itself' perfectly around every positive training point?

**A:** It achieves zero training error but may fail to generalise, resulting in high test error if future positive examples do not perfectly match the training points.

---

## Card 16

**Q:** Term: Supervised Learning

**A:** Definition: A learning paradigm where the algorithm is provided with explicit examples of correct behaviour, consisting of input-output pairs. Example: Training a system to translate English sentences into Spanish using a large database of paired translations.

---

## Card 17

**Q:** Term: Unsupervised Learning

**A:** Definition: A task where the algorithm is given examples without labels and must find regularities or patterns within the data. Example: Grouping customers into different segments based on similar purchasing habits without pre-defined categories.

---

## Card 18

**Q:** Term: Regression

**A:** Definition: A supervised learning task where the target output is a continuous real number rather than a discrete category. Example: Predicting the exact price of a house based on its square footage and location.

---

## Card 19

**Q:** Term: Multi-way Classification

**A:** Definition: A classification task where the model must choose from more than two possible discrete categories. Example: Categorising an image as a 'dog', 'cat', or 'bird' instead of just 'animal' or 'not animal'.

---

## Card 20

**Q:** Term: Active Learning

**A:** Definition: A scenario where the learning algorithm can strategically request labels for specific examples to improve its performance. Example: A medical diagnosis system asking a doctor to label the most ambiguous X-ray images to learn more efficiently.

---

## Card 21

**Q:** Term: Transfer Learning

**A:** Definition: Applying knowledge gained from solving one problem to a different but related task. Example: Using a model trained to translate English to Spanish to help develop a translation system for English to Portuguese.

---

## Card 22

**Q:** Term: Reinforcement Learning

**A:** Definition: A problem of learning to take actions in an environment to maximise a numerical reward or criterion. Example: Training a robot arm to grasp objects by rewarding successful grasps and penalising failures.

---

## Card 23

**Q:** In a self-driving car, what type of machine learning task is being performed when camera input is interpreted to avoid collisions?

**A:** It is a prediction task involving image analysis to identify objects and predict potential future events.

---

## Card 24

**Q:** Why must real-world objects, like movies or images, be converted into feature vectors before being processed by a machine learning algorithm?

**A:** Computers do not 'understand' raw objects; they require numerical representations to perform the mathematical operations needed for classification.

---

## Card 25

**Q:** Term: Semi-supervised Learning

**A:** Definition: A learning approach that combines a small amount of labelled data with a large amount of unlabelled data. Example: Using a few thousand manually categorised news articles and millions of unlabelled ones to build a classifier.

---

## Card 26

**Q:** What is the 'parameter' in the context of supervised learning mappings?

**A:** A variable that defines a specific mapping from the input to the output, which the algorithm adjusts to find the best fit for the training examples.

---

## Card 27

**Q:** In the movie recommender problem, how is a feature vector typically constructed for an individual film?

**A:** By systematically asking a series of questions (e.g., 'Is it a comedy?') and recording the answers as binary or real numbers.

---

## Card 28

**Q:** What does the notation $x^{(i)}$ represent in a training set?

**A:** The feature vector corresponding to the $i^{th}$ training example in the set.

---

## Card 29

**Q:** Why is 'generalisation from training set to test set' described as being at the heart of machine learning problems?

**A:** Because the true goal is to perform well on future, unknown data, not merely to memorise the examples already provided.

---

## Card 30

**Q:** Pitfall: What is the primary disadvantage of using an excessively complex classifier that perfectly fits the training data?

**A:** It often loses the ability to generalise, leading to high error rates on new test examples that differ slightly from the training points.

---

## Card 31

**Q:** How does the machine learning approach differ from 'traditional engineering' when solving complex problems like speech recognition?

**A:** Traditional engineering relies on manually specifying rules, whereas machine learning automates the solution by finding patterns in examples of correct behaviour.

---

## Card 32

**Q:** Term: Structured Output Prediction

**A:** Definition: A learning task where the output is a complex object rather than a simple label or number. Example: Predicting a full sentence as a description for a given input image.

---

## Card 33

**Q:** What information is exclusively available to the learning algorithm during the training phase?

**A:** The training set, which consists of pairs of feature vectors and their corresponding known labels.

---

## Card 34

**Q:** How is a 'bad classifier' typically identified using training error?

**A:** By a high fraction of misclassified examples in the training set compared to other potential classifiers.

---

## Card 35

**Q:** What is the relationship between the 'set of possible classifiers' and the final chosen mapping?

**A:** The set of possible classifiers represents all alternatives considered, from which the algorithm selects the one that best fits the training data while maintaining generalisation.

---

## Card 36

**Q:** In a binary classification plot, what does a 'shaded region' usually represent?

**A:** The area of the feature space that the classifier maps to a specific label, such as $+1$.

---

## Card 37

**Q:** Why is it important to apply the same question procedure to both training and test movies in a recommender system?

**A:** To ensure that the feature vectors are in the same format so the learned classifier can be applied consistently to new movies.

---

## Card 38

**Q:** Pitfall: What common error occurs when a training set is used to evaluate a classifier instead of just training it?

**A:** Over-optimism, where the error rate appears much lower (even zero) than it will be on actual unseen test data.

---

## Card 39

**Q:** How does multi-way classification generalise the concept of labels from binary classification?

**A:** It expands the set of possible labels from two ($+1$ and $-1$) to a larger finite set of categories.

---

## Card 40

**Q:** In reinforcement learning, what is the role of the 'reward' (e.g., successful grasp)?

**A:** It acts as the objective function that the algorithm tries to maximise by adjusting its chosen actions.

---

## Card 41

**Q:** What is the 'input' and 'output' in a machine translation task viewed as a machine learning problem?

**A:** The input is a sentence in the source language (e.g., English), and the output is the corresponding sentence in the target language (e.g., Spanish).

---

## Card 42

**Q:** How can the stock market be used as an example of machine learning for future event prediction?

**A:** Historical stock values are used to predict the value of the stock for the following day.

---

## Card 43

**Q:** What is the significance of the dimensionality of the feature space (e.g., $R^2$)?

**A:** It corresponds to the number of features or attributes assigned to each example in the dataset.

---

## Card 44

**Q:** Term: Hypothesis Class

**A:** Definition: The set of all possible mapping functions (classifiers) that an algorithm considers during the learning process. Example: The set of all possible straight lines that could be drawn to separate data on a 2D plane.

---

## Card 45

**Q:** Why might a learning algorithm seek to find a 'small set of possibilities' that work well on the training set?

**A:** Limiting the number of choices (reducing complexity) helps ensure the chosen model generalises better to unseen test data.

---

## Card 46

**Q:** In the context of the Amazon product review project, what is the primary task for the linear classifier?

**A:** To predict whether a review is positive or negative based solely on the text of the review.

---

## Card 47

**Q:** What determines a 'good' choice of features when feeding data into a linear classifier?

**A:** The ability of those features to clearly represent the differences between the categories being classified.

---

## Card 48

**Q:** What is the core difference between predicting future events and predicting unknown properties?

**A:** Future events haven't happened yet (e.g., next day's stock price), while unknown properties exist but are not yet identified (e.g., whether a molecule is soluble).

---

## Card 49

**Q:** How does Google Translate use machine learning to improve its translations?

**A:** It uses large numbers of example sentence pairs to search for optimal parameter values in a complex mapping between languages.

---

## Card 50

**Q:** What is the 'prediction' being made in a game of Go when machine learning is applied?

**A:** The model predicts the optimal move or the likelihood of winning from a specific board configuration.

---

## Card 51

**Q:** If a training set size is denoted by $N=4$, how many pairs of $(x, y)$ are available to the algorithm?

**A:** Four pairs, each containing one feature vector and its corresponding label.

---

## Card 52

**Q:** In a 2D representation of features, what does each coordinate of the point $(x_1, x_2)$ typically represent?

**A:** Each coordinate represents a specific feature or numerical attribute of the object being classified.

---
