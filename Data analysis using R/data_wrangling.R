# remove all variables and clear console
rm(list=ls())
cat("\014")  

library(tidyverse)
library(forcats)
library(nycflights13)
library(lubridate)


# TIBBLES
# Tibbles is a more modern version of dataframes in R
# Most other R packages use regular dataframes. To convert a dataframe into a tibble, simply use as_tibble()
as_tibble(iris)

# Creating a tibble from individual vectors
tibble(
  x = 1:5,
  y = 1,
  z = x ^ 2 + y
)

# Creating a tibble using tribble(), for transposed tibble. This is customised for data entry.
tribble(
  ~x, ~y, ~z,
  #--/--/---
  'a',2,3.6,
  'b',1,8.5
)

# Subsetting columns
df <- tibble(
  x = runif(5),
  y = rnorm(5)
)

df$x
df[['x']]
df[[1]]

# DATA IMPORT
# using the readr package that is part of tidyverse. 
heights <- read_csv('heights.csv') #read_csv is better than base R's read.csv function

# TIDY DATA
# tidy dataset is basically data that is formatted into a dataframe, where
# each variable has its own column, each observation has its own row, and each value have its own cell

# A common problem is a dataset where columns are not names of variables, but values, e.g.
table4a
# Gathering. To tidy a dataset like this, we'll gather those columns into a new pair of variables
tidy4a <- table4a %>%
  gather(`1999`, `2000`, key = 'year', value = 'cases')

# Tidying another table
table4b
tidy4b <- table4b %>%
  gather(`1999`, `2000`, key = 'year', value = 'population')

# Combining the tidied version of table4a and table4b into a single tibble
left_join(tidy4a,tidy4b)

# Spreading is used to fix datasets where single observations are spread across rows, e.g.:
table2

table2 %>%
  spread(key = type, value = count)

# Separate. Separate() pulls apart one column into multiple columns, by splitting whereever a seperator character appears.
table3

table3 %>%
  separate(col = rate,into = c('cases','population'),sep = '/',convert = TRUE)

# Separating integers
table3 %>%
  separate (col=year, into = c('century','year'), sep = 2, convert = TRUE) # 2 means position from the left

# Unite is the opposite of separate, it combines multiple column into one column
table5

table5 %>%
  unite(col = 'year', century, year, sep = "")

# MISSING VALUES
# Missing values can be explicit (NA), or implicit (the observations is not in the dataset)
# Sometimes missing values should be filled with the last non-missing value, as in:
treatment <- tribble(
  ~ person,           ~ treatment, ~response,
  "Derrick Whitmore", 1,           7,
  NA,                 2,           10,
  NA,                 3,           9,
  "Katherine Burke",  1,           4
)

treatment %>%
  fill(person)

# Data tidying case study - tuberculosis cases around the world
who

# First. Note that many of the columns names are observations, and not variables, This is a common problem with uncleaned dataset.
# Remember, use gather to put these observations into one column.
who1 <- who %>%
  gather(new_sp_m014:newrel_f65, key = 'key',value = 'cases', na.rm = TRUE) %>% # gather 
  mutate(key = stringr::str_replace(key, "newrel", "new_rel")) %>% # replace newrel w/ new_rel so its consistent
  separate(col = key, into = c('temp','cause','sex age'), sep = '_') %>%
  separate(col = `sex age`, into = c('sex','age group'), sep = 1) %>%
  select(-iso2, -iso3, -temp) # drop redundant columns

# Relational data
# It's rare that data analysis involves only a single table of data. Typically, you'd have to combine many tables of data
# Multiple tables are called relational data
# Key verbs when working with relational data:
# Mutating joins, which add new variables to one data frame from matching observations in another
# Filter joins, which filters observations from one data frame based on whether or not they match an observation in the other table
# Set operations, which treat observations as if they were set elements

# Practicing relational data on the nycflights13 package, which 4 more tibbles that related to the 'flights' table 
airlines
airports
planes
weather

# Variables used to connect pairs of tables are called 'keys'. There are two types of keys:
# Primary key uniquely identifies an observation in its own table. 
# Foreign key uniquely identifies an observation in another table.
# In some cases, multiple variables may be needed to uniquely identify an observation (e.g. year, month, AND day)
# Sometimes a table doesn't have an explicit primary key. Each row is an observation, but no combination of variables reliably identifies it
# In these cases, it may be useful to add one called a 'surrogate key'

# Once you've identified the primary key, it's good practice to verify that they do uniquely identify each observation 
# The primary key should appear only once. 
planes %>%
  count(tailnum) %>% # Count the occurences values in the tailnum column.
  filter(n>1) # See if any appears more than once

weather %>% 
  count(year, month, day, hour, origin) %>% 
  filter(n > 1)

# A primary key and the corresponding foreign key in another table forms a relation. Relations are typically one-to-many
# E.g. each flight has one plane, but each plane has many flights

# Mutating join. Combines variables from two tables. It first matches observations by their keys, then copies across variables from one to table to the other

flights2 <- flights %>% # Make the dataset a bit smaller to work with
  select(year:day, hour, origin, dest, tailnum, carrier)

# Adding full airline name to the flights2 data
flights2 %>%
  left_join(airlines, by = 'carrier') # by denotes which variable to use as key

# Inner joins match by key, and drop all observations where keys don't match, so inner drops are not very useful
# Outer joins keep observations that appear in at least one of the tables. There are 3 types of outer joins. If joining x and y:
# A LEFT JOIN keeps all observations in x. Left joins the the most commonly used, when you have to look up some additional info from another table
# A RIGHT JOIN keeps all observations in y
# A FULL JOIN keeps all observations in x and y
# Outer joins fill unmatched observations with NA

# Defining the key columns
# By default, by = NULL, and use all variables that appear on both tables
flights2 %>%
  left_join(weather)

# A character vector, by = "x", or by = c("a" = "b"), using the a column in x and b column in y

# Filtering joins affects observations, not variables
# semi_join(x,y) keeps all observations that have a match in y
# anti_join(x,y) drops all observations that have a match in y

# Semi_join is useful for matching filtered summary tables back to original rows. For example, top ten destinations
top_dest <- flights %>%
  count(dest,sort = TRUE) %>%
  head(10)
# Now find all flights that went to these destinations
flights %>%
  semi_join(top_dest)

# Anti_join is useful for testing mismatches between two data tables

# STRINGS
string <- 'this is a string'
str_c('a','b') # combined strings

# Regular Expressions (regexps). Basic matches
x <- c('apple','banana','pear')
str_view(x, 'an')

# Visualize matching with wildcard
str_view(x,'.a.')

# Visualizing matching the beginning or the end of a string with anchors
str_view(x,'^a')
str_view(x,'a$')

# Detect string matches
str_detect(x, 'e')

# How many common words start with t?
sum(str_detect(words, '^t'))

# What proportion of common words end with a vowel?
mean(str_detect(words, '[aeiou]$'))

# Skipped more complicated exercises working with string data

# FACTORS
# To work with factors, first have to create the levels
month_levels <- c(
  "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
)

x1 <- c('Dec','Apr','Jan','Mar') #This is just strings
x2 <- factor(x1, levels = month_levels) #This is factors
sort(x2) #Factors can be sorted

# Factors can be created without creating the levels, but just pulling them from the data
f1 <- factor(x1, levels = unique(x1))

# Working with factors in the general social survey (GSS) dataset
gss_cat

# To see what's in a column
gss_cat %>%
  count(race)

# Changing the factor order
# Example, hours of tv viewed by religion
relig_summary <- gss_cat %>%
  group_by(relig) %>%
  summarise(tv = mean(tvhours, na.rm = TRUE),
            age = mean(age, na.rm = TRUE),
            n = n()
  )

# It is difficult to see patterns without sorting/changing the order of factors
ggplot(relig_summary,aes(tv,relig)) + geom_point()

# fct_reorder(f,x) takes two arguments: f, the factor to be ordered, and x, the vector used to sort/reorder f
ggplot(relig_summary,aes(tv,fct_reorder(relig,tv))) + geom_point()

# fct_relevel(f,x) takes f, factor to be releveled, and x, any number of items to be put in the front of the factor order
# fct manipulations can also be done before plotting
income_summary <- gss_cat %>%
  group_by(rincome) %>%
  summarise(age = mean(age, na.rm = TRUE)) %>%
  mutate(rincome = fct_relevel(rincome,'Not applicable'))

ggplot(income_summary,aes(age,rincome)) + geom_point()

# fct_relevel2 is useful for lining up order of legends with colored line plots

# Changing the value of factor levels (useful for correct labels for publications)
gss_cat %>%
  mutate(partyid = fct_recode(partyid,
                              "Republican, strong"    = "Strong republican",
                              "Republican, weak"      = "Not str republican",
                              "Independent, near rep" = "Ind,near rep",
                              "Independent, near dem" = "Ind,near dem",
                              "Democrat, weak"        = "Not str democrat",
                              "Democrat, strong"      = "Strong democrat")) %>%
  count(partyid)

# Changing the value of factor levels is also useful for merging two factors into one.
# Simply change the values of different factors into the same value
# fct_collapse() is another function for when there are many variables (not shown here)
gss_cat %>%
  mutate(partyid = fct_recode(partyid,
                              "Republican, strong"    = "Strong republican",
                              "Republican, weak"      = "Not str republican",
                              "Independent, near rep" = "Ind,near rep",
                              "Independent, near dem" = "Ind,near dem",
                              "Democrat, weak"        = "Not str democrat",
                              "Democrat, strong"      = "Strong democrat",
                              "Other"                 = "No answer",
                              "Other"                 = "Don't know",
                              "Other"                 = "Other party"
  )) %>%
  count(partyid)

gss_cat %>% count(relig)

# DATE AND TIMES
today()
now()

# Parsing strings into date or datetime format
ymd('2017/1/2')
dmy('1 June 2016')

# Creating datetime from individual components in a df
flights %>%
  select(year,month,day,hour,minute) %>%
  mutate(departure = make_datetime(year,month,day,hour,minute)) %>%
  ggplot(aes(departure)) + geom_freqpoly(binwidth = 86400) #binwidth = 86400s = 1 day

# Components of date time 
# getting components
dt <- ymd_hms("2016-07-08 12:34:56")
year(dt)
month(dt)
second(dt)
wday(dt)
yday(dt)

# Using wday to see flights over the week
flights %>%
  select(year,month,day,hour,minute) %>%
  mutate(departure = make_datetime(year,month,day,hour,minute)) %>%
  mutate(wday = wday(departure, label = TRUE)) %>%
  group_by(wday) %>%
  ggplot(aes(wday)) + geom_bar()

# Setting components of datetime
dt
year(dt) <- 1999
dt

# application, for example, set yday for all observations to 1, then visualize all days of the year in one graph showing flights in 24 hours

# Skipped time spans
