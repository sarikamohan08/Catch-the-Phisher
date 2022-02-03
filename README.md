# PhishingClassifier
### Buisness Problem:
     Phishing is the fraudulent attempt to obtain sensitive data, such as usernames, passwords by disguising a fake website
     as a trustworthy website.Therefore identifying Phishing websites maximizes internet security.
### Target Variable: Result
    If Result = 0, Not a Phishing website
    If Result = 1, Phishing website.
    
Data is having 30 predictor attributes and one response variable with binary classes. 0 out of 2456 records is missing for all columns.1362 records are of trust-worthy websites(majority class) and  1094 records are Phishing websites(Minority class)
![Resultcount](https://user-images.githubusercontent.com/60782716/87672405-84799500-c790-11ea-95cf-270642efe661.PNG)

The datatype of predictors are taken as int64, Howerver the predictors are nominal. Therefore Quantitative analysis like correlation has no or less signficance.

### Exploratory Data analysis
Since predictors are categorical, they are plotted as Bivariate countplots  where class labels are represented as color of the bars.

![features1](https://user-images.githubusercontent.com/60782716/87689485-e2fd3e00-c7a5-11ea-8f8d-7c3705bb7c92.PNG)

![features2](https://user-images.githubusercontent.com/60782716/87690496-2ad09500-c7a7-11ea-802c-7512518e5816.PNG)

Looking at the plots we can see that Features like SSL_Final_state, web_traffic,Domain_registeration_length, URL_of_anchor have a greater difference between the classes. 
And Almost all features are having atleast some difference between two classes. So these variances must be captured.



Chi_Squared test is used to find the relationship between categorical features by measuring their independence.
We hypothesize H0:Feature is independent of Result as our null statement
We choose our p-value level to 0.05, If the p-value test result is more than 0.05 we fail to reject the Null Hypothesis. This means, there is no relationship between the feature  and Result feature based on the Chi-Square test of independence.
For the features 'Statistical_report','Iframe','popUpWidnow','on_mouseover','Submitting_to_email','HTTPS_token','port','Favicon','having_At_Symbol' we fail to reject the Null hypothesis. So they are droped
### Model Selection
By using Kfold Cross Validation we compare different models.
![Model accuracies](https://user-images.githubusercontent.com/60782716/87711717-49458900-c7c5-11ea-9976-36e855051847.PNG)

KnearestNeighbors and RandomForest models have Greater accuracy and less standard deviation.So these models are taken for Tuning
Before Hyper parameter Tuning, Principal component analysis is useful here to reduce the dimensions. The last 8 dimensions which doesn't have much variance is dropped.
Since there is an imbalance between classes model will be biased towards the majority class, Inorder to rectify that Synthetic Minority Over-sampling Technique (SMOTE)  is applied.
Now using GridSearch Best Parameters for both Algorithms are obtained.

### Model Efficiency
 #### Random Forest:
    The model had a Training accuracy of  0.9944289693593314 and Testing accuracy of 0.9857723577235772
                 precision    recall  f1-score   support

               0       0.99      0.99      0.99       285
               1       0.98      0.99      0.98       207

        accuracy                           0.99       492
       macro avg       0.99      0.99      0.99       492
    weighted avg       0.99      0.99      0.99       492
    The Roc curve is given below:
    
  ![aucrf](https://user-images.githubusercontent.com/60782716/87716546-9a0cb000-c7cc-11ea-8d73-e5f211b9342e.PNG)
    
    
    
  #### KNN:
    The model had a Training accuracy of  0.9935004642525533 and Testing accuracy of0.979674796747967
    
    
                    precision    recall  f1-score   support

               0       1.00      0.97      0.98       285
               1       0.96      1.00      0.98       207

        accuracy                           0.98       492
       macro avg       0.98      0.98      0.98       492
    weighted avg       0.98      0.98      0.98       492
    The Roc curve is given below:

 ![aucknn](https://user-images.githubusercontent.com/60782716/87716534-9711bf80-c7cc-11ea-9b04-84456b1c02fb.PNG)





#### Since the Recall of minortity class ie Result=1 is more important to the business problem KNN is our final model


 
