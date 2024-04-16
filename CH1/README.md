# Chapter 1

The following section visualizes and explains the concepts described in Chapter 1 of the Bishop Textbook. Here I will explain the basics of Bayes' theory and finding its application in polynomial curve fitting.

# Polynomial Curve Fitting

<div align="center">
  <img src="https://github.com/Jayant74/Bishop-Textbook-Concepts/assets/129622540/dcc516ee-16de-46bd-8472-9780c8168f2e" width="500" alt="Sample Image">
  <br>
  <p>Figure 1. Noisy sine wave data</p>
</div>

Given a dataset, we would like to find its underlying pattern. In other words, we want to learn a function that maps a dataset value 'x' to its corresponding result, 'y' _and_ is able to predict the resulting value given a new data point. The example from the textbook is a noisy sine wave, visualized in figure 1.   

<div align="center">
  <img src="https://github.com/Jayant74/Bishop-Textbook-Concepts/assets/129622540/655c92e1-1c6f-467d-8b21-dd6da93fc1cf" width="500" alt="Sample Image 2">
  <br>
  <p>Figure 2. Polynomial curve fitting with gradient descent</p>
</div


The textbook takes its time, and justifiably so, to arrive at an important conclusion. Maximizing the Log Likeliehood function of a _Gaussian_ dataset is equivalent to minimizing the Sum of Squared Error function. This conclusion is extraordinary, however, there are some key properties to make this parallel work. First, the definition of the Gaussian stands on satisfying two properities. The motivation is as follows. Say we want to know the probability of an x,y-coordinate.

  - First property: We want to know the probabili of _only the distance_ a point will be from the origin

$$
p(x,y) = p(r)
$$

  - Second property: x, and y are independent of each other. That is, if you learn the x-coordinate, that gives you no information about the y-coordinate

The second property implies that the joint distribution of x, and y is equal to the product of their respective distributions:

$$
p(x,y) = p(x)p(y) = p(\sqrt{x^{2} + y^{2}} = p(r)
$$

I will include the derivation of the Gaussian at a later date, but even from the equation above, we can see the distance of the (x,y)-coordinate is the same as calculating a _radius_ of a circle. This is why a _\pi_ ends up in the Gaussian equation:

$$
N(x|\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}exp{-\frac{1}{2}{\frac{(x-\mu)^2}{\sigma^2}}}
$$

The definition of the Gaussian relies on the parameters \mu, which is the origin from which the distance 'r' is calculated, and the parameter \sigma which can be thought of as the spread or deviation from the mean. 

So, why does satisfying these two properties make the Gaussian useful? And how does it aid in its parallel to minimizing the Sum of Least Squares?
