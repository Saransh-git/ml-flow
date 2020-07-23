We might be familiar with the classic steps in a Data Science workflow which goes like following:-

1) Clarify on the business use case and how the stakeholders are going to use your model
2) Frame the business problem to a Machine Learning problem
3) Decide on an evaluation metric/ cost function/ loss function
4) Decide on the model baseline and a performance threshold for the final model
5) Glance through the data to verify the assumptions in line with the business use case
6) Split train, validation, test. The test data should never be seen by your model before the final run and 
the model hyperparams shouldn't be adjusted based on metric obtained on the test set.
7) Preprocess data, engineer features either by feature selection or introducing new features
8) Fine tune the model based on validation or cross-validation or out-of-bag sample error. Do not forget to check the
confidence of the evaluation metric obtained as a single point value can often be misleading.
9) Select the best model, and there you go! You now have successfully trained an ML model.

So, what next? Remember the business objective, how are we going to transfer what our model has just learnt to user
experience. Machine Learning is a tool which adds value to your business use case and not every problem needs to be 
solved using Machine Learning if a simple rule based or analytical model can achieve an equivalent amount of 
performance, why complicate things up then? And just like other engineering systems, for a Machine Learning based
solution to add value to a business, it needs to touch base with the users.

Secondly, it is also important to understand that a Machine Learning system is a derived one unlike an instruction based
software. While an instruction based software would perform the way the instructions are written forever, a ML system
on the other hand would perform at best based on the data it is trained upon. In a perfect static environment, the once
trained ML system would be alike an instruction based system, but we live in an ever changing world! The way users 
interact with the system change and hence, the user events which is produced. 

Thirdly, as an engineering proponent, I often find the lack of modularity and reproducibility in ML workflow. Due to
Machine Learning's iterative nature, it makes these principles all the more important to be incorporated.

While an evaluation metric helps us decide which ML model, configuration, features are performing better and should 
always be chosen carefully, but often the chosen metric doesn't translate directly to the business KPI. This calls up 
for an evaluation approach which measures the KPI directly. Wait what, shouldn't the performant model be decided not
based on the production data. While this still holds true, there can be multiple candidate performant models and 
choosing one out of them for deployment directly might not be the best foot forward. I suggest passing them through a 
split test experimentation funnel wherein the control group should always be the one without the aid of any ML model. 
The control group here is an important one to help answer if Machine Learning is useful at all for the use case or not. 

Lastly, the data which ML model is trained upon originates based on how user interacts with the environment, product and
there are likely other factors into play which impacts user behavior. This results in a data drift as the training data 
differs in its distribution to what the user activities produce. Therefore, one should always update model either on a 
periodic interval or on an event driven signal when performance drops below a certain threshold. Even best, if your 
system supports training on-the-fly and your use case needs it.

So, here I propose the five design principles to a Machine Learning System:-

- **Integrate**
- **Automate**
- **Reproduce**
- **Experiment**
- **Audit**

Integration is the foremost one which kind of makes way to the other principles and basically reiterates the fact that
for Machine Learning as a tool to be useful, it needs to be incoprporated into an application which the users interact 
with directly or indirectly based on the outcomes produced by the ML system.

Automation follows from the iterative nature along the ML workflow and promotes rapid iterations across various 
configurations, features, models and of course the underlying historical data.

Reproducibility brings in modularity into the workflow and result an ease in debugging, process management and 
provenance across data lineage. Again, it's modularity which supports the rapidness in the second pillar and provides 
much needed transparency across teams. Moreover, it further facilitates agile development into ML solutions. Often 
different teams work on similar features, and therefore this pillar removes redundancy along the pipeline.

Experimentation assures that the ML system developed indeed fulfils the business use case which it's derived upon. It 
serves as a check-mark to the earlier decided baseline and performance threshold.

Audit is an important step along the pipeline. The performance of your ML system keeps deteriorating over time as the 
training data keeps on growing older and older. For the system to keep performing, it's as important to not just 
consider the fresh data over time, but research upon features to capture new kinda user interactions.

On an ending note, the pillars compose a major chunk to what seems from outside a ML code responsible for  all the 
magic, and I would keep on saying that it's never a magic and enabling the infra is the greatest good to building many 
more Machine Learning Applications.
