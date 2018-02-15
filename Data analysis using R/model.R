# remove all variables and clear console
rm(list=ls())
cat("\014")  

library(tidyverse)
library(modelr)
options(na.action = na.warn)

# A simple model
ggplot(sim1, aes(x,y)) +
  geom_point()

# Making some random models
models <- tibble(
  a1 = runif(250,-20,25),
  a2= runif(250,-5,5)
)
ggplot(sim1, aes(x,y)) +
  geom_point() +
  geom_abline(data = models, mapping = aes(intercept = a1, slope = a2), alpha = 1/4)

# Skipped manual way of finding best model

# Using linear model (lm) to fit
sim1_mod <- lm(y ~ x, data = sim1)
coef(sim1_mod)

ggplot(sim1, aes(x,y)) +
  geom_point() +
  geom_abline(data = models, mapping = aes(intercept = 4.22, slope = 2.05), alpha = 1/4)

# Skipped residuals and other sections

# MODEL BUILDING
library(nycflights13)
library(lubridate)
library(hexbin)

# Surprisingly, low quality (cut color clarity) diamonds cost more. 
ggplot(diamonds, aes(cut, price)) + geom_boxplot()
ggplot(diamonds, aes(color, price)) + geom_boxplot()
ggplot(diamonds, aes(clarity, price)) + geom_boxplot()

# is this because there is a confounding factor, carat?
# carat (weight of diamonds) strongly predicts price
ggplot(diamonds, aes(carat, price)) + 
  geom_hex(bins = 50)

# we can build a model to separate out the effect of carat and see how the other features affect price
# first, make 2 changes. filter out outliers and log transform carat and price 
diamonds2 <- diamonds %>%
  filter(carat <= 2.5) %>%
  mutate(lprice = log2(price), lcarat = log2(carat))

# log transform is useful because it makes the pattern linear, and linear relationships are easy
ggplot(diamonds2, aes(lcarat,lprice)) +
  geom_hex(bins = 50)

mod_diamond <- lm(lprice ~ lcarat,data = diamonds2)

# skipped using grid 

# MANY MODELS
# Advanced. skipped