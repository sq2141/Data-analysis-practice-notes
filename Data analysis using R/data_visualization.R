# clear workspace and console
rm(list=ls())
cat('\014')

# load package (on first run)
# library(tidyverse)

# Creating a ggplot
# ggplot() initiates a coordinate system where data is overlaid, and takes data to be used in the graph
# The + at the end is a ggplot specific notation
# geom_point() function adds a layer of points onto the graph (scatterplot)
# Each geom function takes a mapping argument: how data variables are mapped to aesthetics
# mapping argumenet is always, mapping = aes()
ggplot(data=mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy, color=class))

# FACETS are subplots each display a subset of data (separates out data by some variable to more easily see their patterns)
# To 'facet' a plot by a variable, use facet_wrap()
ggplot(data=mpg) + 
  geom_point(mapping = aes(x=displ, y=hwy)) +
  facet_wrap(~ class)

# FACET by two variables
ggplot(data=mpg) +
  geom_point(mapping=aes(x=displ, y=hwy)) +
  facet_wrap(drv ~ cyl)

# Plotting data using different geoms
# GEOMs are geometric objects used to represent the data. i.e. bar graphs use bar geoms, boxplots use box geoms
ggplot(data=mpg) +
  geom_smooth(mapping=aes(x=displ, y=hwy, linetype=drv, color = drv)) +
  geom_point(mapping=aes(x=displ, y=hwy, color=drv))

# For many geoms where a single geometric object represents multiple rows of data, grouping the data by some variable just requires
# a mapping of an aesthetic to that variable, and it'll plot them separately automatically.
ggplot(data=mpg) +
  geom_smooth(mapping=aes(x=displ,y=hwy, color=drv),show.legend=FALSE)

# When displaying multiple geoms in the same plot, it's good practice to put the arguments shared across the geoms inside ggplot()
# any arguments inside the individual geoms just overrides that particular geom
ggplot(data = mpg, mapping=aes(x=displ, y=hwy)) +
  geom_point(mapping = aes(color=class)) + 
  geom_smooth()

# STATISTICAL TRANSFORMATIONS (aka graphs that plot statistical summaries)
# Bar graph where the height of the bar is the count of occurence the in the dataset
ggplot(data=diamonds) +
  geom_bar(mapping=aes(x=cut))

# Bar graph where the height of the bar is the value, in this case, explicitly declare the stat argument
demo <- tribble(
  ~cut,         ~freq,
  "Fair",       1610,
  "Good",       4906,
  "Very Good",  12082,
  "Premium",    13791,
  "Ideal",      21551
)
ggplot(data = demo) +
  geom_bar(mapping=aes(x=cut,y=freq),stat='identity')

# Bar graph where the height is proportion, rather than count
ggplot(data=diamonds) +
  geom_bar(mapping=aes(x=cut,y=..prop..,group=1))

# Coloring border or filling bar geoms
ggplot(data=diamonds) + 
  geom_bar(mapping=aes(x=cut, color=cut))

ggplot(data=diamonds) + 
  geom_bar(mapping=aes(x=cut, fill=cut))

# Mapping the fill aesthetic to a different variable creates stacked bars
ggplot(data=diamonds) + 
  geom_bar(mapping=aes(x=cut, fill=clarity))

# Stacked proportion bar graphs (add up to 1)
ggplot(data=diamonds) + 
  geom_bar(mapping=aes(x=cut, fill=clarity), position='fill')

# Grouped bar graphs
ggplot(data=diamonds) +
  geom_bar(mapping=aes(x=cut, fill=clarity), position='dodge')

# For scatterplots, datapoints may overlap, so use jitter to add some noise to spread out the datapoints
ggplot(data=mpg) +
  geom_point(mapping=aes(x=displ,y=hwy), position='jitter')

# COORDINATE SYSTEMS
# Switching the x and y axis (coord_flip())
ggplot(data = mpg, mapping = aes(x = class, y = hwy)) + 
  geom_boxplot() +
  coord_flip()

# Correct aspect ratio (same spacing between x and y axis) using coord_quickmap()
# Skipped

# Polar coordinates (a circle) using coord_polar()
bar <- ggplot(data=diamonds) +
  geom_bar(mapping=aes(x=cut,fill=cut), show.legend = FALSE, width=1) +
  theme(aspect.ratio = 1) +
  labs(x=NULL, y=NULL)

bar + coord_flip() # tip: can quickly change between dif plots if set ggplot to bar first
bar + coord_polar()

