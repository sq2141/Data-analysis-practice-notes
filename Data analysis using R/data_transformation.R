# clear workspace and console
rm(list=ls())
cat('\014')

# load stuff
# library(tidyverse)
# library(nycflights13)

# dplyr package for data manipulation. each function is a verb that describes what you do to the data
# 1. pick observations by their values (filter())
# 2. reorder the rows (arrange())
# 3. pick variables by their names (select())
# 4. create new variables with functions of existing variables (mutate())
# 5. collapse many values down to a single summary (summarise())
# these can all be used in conjunection with group_by() which changes the scope of each function
# the first argument is dataframe, the subsequent arguments describe what to do with it. the result is a new dataframe
# dplyr never modifies the inputs, so if you want to save the results, you'll have to save it to a variable

flights

# Filter rows with filter()
# sidenote: wrapping an assignment in brackets both assigns and prints it out, otherwise it only assigns it
(jan1 <- filter(flights, month == 1, day == 1))

# Filtering with multiple conditions using boolean operators
filter(flights, month == 11 | month == 12)

# A useful shorthand for filtering many conditions is with %in% (read as 'contain')
filter(flights, month %in% c(11,12))

# NAs are excluded in filter, if you want to preserve them, have to ask for that explicitly
df <- tibble(x=c(3,NA,5))
filter(df, is.na(x) | x>4)

# Arrange rows with arrange()
arrange(flights,year,month,day)
arrange(flights, desc(arr_delay))

# Select chooses a subset of columns/variables. 
select(flights,year,month,day)
select(flights,year:day)
select(flights,-(year:day))

# Helper functions such as starts_with, ends_with, contains, matches, num_range etc.
select(flights,starts_with('dep'))

# Renaming a column
rename(flights, tail_num = tailnum)

# Everything helper function to move columns to the beginning of the df
select(flights, time_hour, air_time, everything())

# Mutate adds new columns that are functions of existing columns
flights_sml <- select(flights,
                      year:day,
                      ends_with('delay'),
                      distance,
                      air_time)

mutate(flights_sml,
       gain = arr_delay - dep_delay,
       speed = distance/air_time*60)

# If you only want to keep the new columns, use transmute()
transmute(flights_sml,
          gain = arr_delay - dep_delay,
          hours = air_time / 60,
          gain_per_hour = gain/hours)

# group_by and summarise
# summarise calculates a summary across all the rows, which by itself is not very useful
summarise(flights, delay = mean(dep_delay,na.rm=TRUE))

# unless we pair it with group_by, which changes the unit of analysis from the complete dataset to individual groups.
# then when we use dplyr verbs on a grouped dataframe, the analysis is done on the groups
by_day <- group_by(flights, year, month, day)
summarise(by_day, delay = mean(dep_delay,na.rm=TRUE)) # means rows within the same day AND month AND year.

# Combining multiple operations with a pipe
# Looking at flight delays vs. distance to destination
by_dest <- group_by(flights,dest) # Group flights by destination
delay_summary <- summarise(by_dest, # Summarize to commute the mean delay and distance for each dest.
                           delay = mean(arr_delay,na.rm=TRUE),
                           dist=mean(distance,na.rm=TRUE),
                           count=n()) #n() counts how many are in each group?

ggplot(data=delay_summary, mapping=aes(x=dist,y=delay)) +
  geom_point(aes(size=count), alpha=.3) +
  geom_smooth(se=FALSE)
  
# Instead of going through multiple steps and naming the output of each step, use pipes, %>%
# %>% reads as 'then'
delays <- flights %>%
  group_by(dest) %>%
  summarise(delay = mean(arr_delay,na.rm=TRUE),
            dist=mean(distance,na.rm=TRUE),
            count=n()) #good idea to include account whenever you do aggregation

ggplot(data=delay_summary, mapping=aes(x=dist,y=delay)) +
  geom_point(aes(size=count), alpha=.3) +
  geom_smooth(se=FALSE)

# Instead of always removing NAs, can filter them out before working with the data
not_cancelled <- filter(flights,!is.na(dep_delay),!is.na(arr_delay))

not_cancelled %>%
  group_by(year,month,day) %>%
  summarise(mean = mean(dep_delay))

# Looking at flight delays of individual planes (by their tail number)
delays <- not_cancelled %>%
  group_by(tailnum) %>%
  summarise(delay = mean(arr_delay))

ggplot(data=delays,mapping=aes(x=delay)) +
  geom_freqpoly()

# Look at number of flights by each plane vs. delay
delays <- not_cancelled %>%
  group_by(tailnum) %>%
  summarise(delay = mean(arr_delay), count=n()) %>% # Integrating ggplot into pipe
  ggplot(mapping=aes(x=count,y=delay)) +
  geom_point(alpha=.1)

delays

# Other useful summaries
# logical subsetting. e,g, mean(x[x]>0). mean of positives
# sd. standard deviation., min, max,

# Ungroup() to ungroup and return to using operations on ungrouped data

# In addition to grouping and summarising, grouping can also be used together with mutate

# Findin the worst members of each group
flights_sml <- flights %>%
  group_by(year, month, day) %>%
  filter(rank(desc(arr_delay))<10)
