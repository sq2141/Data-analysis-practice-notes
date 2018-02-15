# remove all variables and clear console
rm(list=ls())
cat("\014")  

# PIPES
# pipes %>% are from the magrittr package. also in tidyverse automatically
library(magrittr)
library(tidyverse)

# pipes are like 'then', where the next step in the pipe operates on the outcome of the previous line
# this saves time/space by skipping naming intermediate variables

# Normally, %>% suppresses displaying the current value in the operation, to display it, use %T>%
rnorm(100) %>%
  matrix(ncol = 2) %T>%
  plot() %>%
  str()

# FUNCTIONS
# Functions automate common tasks

rescale01 <- function(x) {
  rng <- range(x, na.rm = TRUE, finite = TRUE)
  (x - rng[1]) / (rng[2] - rng[1])
}

x <- c(1:10, Inf)
rescale01(x)

# If statements. The condition must evaluate to TRUE or FALSE
if (a==2) {
  # Do something
  b <- 1 
} else {
    # Do something else
    b <- 2
}

# If there are many conditional paths, use the switch function

#> function(x, y, op) {
#>   switch(op,
#>     plus = x + y,
#>     minus = x - y,
#>     times = x * y,
#>     divide = x / y,
#>     stop("Unknown op!")
#>   )
#> }

# Setting a default value for your function
# Compute confidence interval around mean using normal approximation
mean_ci <- function(x, conf = 0.95) {
  se <- sd(x) / sqrt(length(x))
  alpha <- 1 - conf
  mean(x) + se * qnorm(c(alpha / 2, 1 - alpha / 2))
}

# Good practice to add sanity checks into your functions
wt_mean <- function(x, w) {
  if (length(x) != length(w)) {
    stop("`x` and `w` must be the same length", call. = FALSE)
  }
  sum(w * x) / sum(w)
}

# The return value of a function is usually the last statement it evaluates
# If you want to return early or explicity state the return value, use return()

# VECTORS
# R has two types of vectors
# 1) Atomic vectors are homogenous (just integers, logicals, doubles etc.)
# 2) Lists are heterogeneous, and can contain any type of data, even other lists
# Besides its values, each vector has 2 properties, its type and length
typeof(letters)
someNumbers <- c(1,222,31)
length(someNumbers)

# Changing vector data types skipped

# Naming vectors
# Naming vectors at creation
a <- c(x = 1, y = 5, z = 3)
a
# Naming after 
library(tidyverse)
set_names(1:3, c("a", "b", "c"))

# In tibbles, we subset using filter(), to generally subset in R, use []
# Subsetting by position
x <- c("one", "two", "three", "four", "five")
x[c(3, 2, 5)]

# Subsetting w/ logical vector
x <- c(2, NA, 3)
x[!is.na(x)]

# Subset with names (if it's a named vector)
x <- c(abc = 1, def = 2, xyz = 5)
x[c("xyz", "def")]

# Lists (aka recursive vectors)
# Creating a list
x <- list(1,2,5)

# attributes are metadata that you can assign to vectors. like class, dimensions etc. skipped
# str() returns the structure of the list
str(x)

# named lists
x_named <- list(a = 1, b = 2, c = 3)
str(x_named)

# lists can contain mixed data types
y <- list("a", 1L, 1.5, TRUE, list(1,9,4,2))
str(y)

# subsetting list is similar to subsetting a vector
a <- list(a = 1:3, b = "a string", c = pi, d = list(-1, -5))

# single square brackets just returns a smaller list containing what you subsetted
str(a[1])

# double square brackets actually extracts the value alone, removing a level of hierarchy from the list
str(a[[1]])

# getting one value in the above example 
a[[1]][2]

# $ extracts named elements from a list, and works like [[]]
a$a
str(a$a)

# Dates, factors, and tibbbles are also vectors

# ITERATION
# For loops. Suppose we want to calculate the median for each column
df <- tibble(
  a = rnorm(10),
  b = rnorm(10),
  c = rnorm(10),
  d = rnorm(10)
)

# Declare a vector to store the results as doubles
output <- vector("double", ncol(df))
for (i in seq_along(df)) {
  output[[i]] <- median(df[[i]])
}
output

# For loop variations
# applying a function with for loops
for (i in seq_along(df)) {
  df[[i]] <- rescale01(df[[i]]) # Use [[]] for things inside list or df to be safe
}
df

# Iterating over names skipped
# Unknown output length skipped

# Use while loop for unknown iteration lengths

# functionals. a for loop can be put inside a function. also, a second variable, in this case fun, can be used to generalize what the function does
# e.g. calculate mean or mediam
col_summary <- function(df, fun) {
  out <- vector("double", length(df))
  for (i in seq_along(df)) {
    out[i] <- fun(df[[i]])
  }
  out
}
col_summary(df, median)
col_summary(df, mean)

# map functions skipped.
# walk skipped