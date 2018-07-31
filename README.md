## TRIBE Coding Challenge


### Background:

TRIBE is a marketplace that assists social media influencers monitise their social media posts through
paid collaborations with brands. A social media influencer is someone with an audience >3000 followers
on Instagram. Brands pay social media influencers to promote their products and services through
sponsored posts to the influencers social media channel and audience. The social media influencer can
choose to promote the brand using static images, through motion using video and audio.

### Context:

Social media Influencers have been basing the price of their social media post on a single post basis. So
If a brand required 10 posts (for example spread over a period) then they would be charged 10x the cost
of a single post. TRIBE has decided to allow social media influencers to sell posts in bundles and charge
the brand on a per bundle basis. So if the Influencer sold image based posts in bundles of 5 and 10 and
brand ordered 15 they would get a bundle of 10 and a bundle of 5.

### Submission Files:
**main.py** - Run modules on document test case

**tribe.py** - Module containing reusable codes

**TRIBE-Test_Breakdown.ipynb**- jupyter-notebook documenting the steps taken in developing the code 


### Task:

Given a brands order, you are required to determine the cost and bundle breakdown for each submission
format. For simplicity, each order should contain the minimal number of bundles.

### Input:

Each order has a series of lines with each line containing the number of items followed by the submission
format code

An example input: 

**10 IMG 15 FLAC 13 VID**

### Output:

A successfully passing test(s) that demonstrates the following output: (The format of the output is not
important)

10 IMG $800

    1 x 10 $800

15 FLAC $1957.50

    1 x 9 $1147.50

    1 x 6 $810

13 VID $2370

    2 x 5 $1800

    1 x 3 $570