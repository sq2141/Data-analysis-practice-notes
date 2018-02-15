# clear workspace and console
rm(list=ls())
cat('\014')

# VISUALIZING DISTRIBUTIONS
# Bar chart (categorical variable)
ggplot(data = diamonds) +
  geom_bar(mapping=aes(x = cut))
# If we want to get the actual number in each bar
diamonds %>%
  count(cut)

# Histogram
ggplot(data = diamonds) +
  geom_histogram(mapping = aes(x = carat), binwidth = .5)
# If we want to get the actual number in each bin
diamonds %>%
  count(cut_width(carat,0.5)) # the cut_width refers to the bin, has nothing to do with diamonds

# Frequency plot (like histogram, but uses lines instead of bars, easy to visualize multiple distributions)
smaller <- diamonds %>% # A standardized frequency plot is called a density plot (see later below)
  filter(carat<3)

ggplot(data = smaller) +
  geom_freqpoly(mapping = aes(x = carat, colour = cut), binwidth = 0.1)

# MISSING VALUES
diamonds2 <- diamonds %>% 
  mutate(y = ifelse(y < 3 | y > 20, NA, y)) #Replacing certain values (that you determine to be errors) with NA 

# COVARIATION
# For example, looking at the relationship between diamond cut and price
# Density plots are frequency plots that have been standardized so the area under the curve for each group adds up to 1
ggplot(data = diamonds, mapping = aes(x = price, y = ..density..)) +
  geom_freqpoly(mapping = aes(colour = cut), bindwidth = 500)

# Boxplots
ggplot(data = diamonds, mapping = aes(x = cut, y = price)) +
  geom_boxplot()

# Two categorical variables (skipped)

# Two continuous variables
# Scatterplot with geom_point
ggplot (data = diamonds) +
  geom_point(mapping = aes(x = carat, y = price), alpha = .01)

# Large datasets can be hard to see with scatterplots, adding transparency w/ alpha helps, or can also bin in 2d
ggplot (data = smaller) +
  geom_bin2d(mapping = aes(x = carat, y = price))

# install.packages('hexbin')
#ggplot (data = smaller) +
#  geom_hex(mapping = aes(x = carat, y = price))

# Or can bin one continuous variable into a categorical variable
ggplot (data = smaller, mapping = aes(x = carat, y = price)) +
  geom_boxplot(mapping = aes(group = cut_width(carat, .1)))

# ggplot can be more succintly written without explicitly declaring the data = , and mapping = arguments, and x and y in aes() 
ggplot(diamonds,aes(cut)) +
  geom_bar()
