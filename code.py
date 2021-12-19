import re
 
page7="Begin the morning by saying to thyself, I shall meet with  the busy—body, the ungrateful, arrogant, deceitful, envious,  unsocial. All these things happen to them by reason of their  ignorance of what is good and evil. But I who have seen the nature  of the good that it is beautiful, and of the bad that it is ugly, and  the nature of him who does wrong, that it is akin to me, not only of  the same blood or seed, but that it participates in the same  intelligence and the same portion of the divinity, I can neither be  injured by any of them, for no one can ﬁx on me what is ugly, nor  can I be angry with my kinsman, nor hate him, For we are made  for co—operation, like feet, like hands, like eyelids, like the rows of  the upper and lower teeth. To act against one another then is  contrary to nature; and it is acting against one another to be vexed  and to turn away.  Whatever this is that I am, it is a little ﬂesh and breath,  and the ruling part. Throw away thy books; no longer distract  thyself: it is not allowed; but as if thou wast now dying, despise the  ﬂesh; it is blood and bones and a network, a contexture of nerves,  veins, and arteries. See the breath also, what kind of a thing it is,  air, and not always the same, but every moment sent out and  again sucked in. The third then is the ruling part: consider thus:  Thou art an old man; no longer let this be a slave, no longer be  pulled by the strings like a puppet to unsocial movements, no  longer either be dissatisﬁed with thy present lot, or shrink from  the future.  All that is from the gods is full of Providence. That which is  from fortune is not separated from nature or without an  interweaving and involution with the things which are ordered by  Providence. From thence all things ﬂow; and there is besides  necessity, and that which is for the advantage of the whole  universe, of which thou art a part. But that is good for every part  of nature which the nature of the whole brings, and what serves to  maintain this code of nature.".split("  ")
 
page8="Now the universe is preserved, as by the changes of the  elements so by the changes of things compounded of the elements.  Let these principles be enough for thee, let them always be ﬁxed  opinions. But cast away the thirst after books, that thou mayest  not die murmuring, but cheerfully, t1uly, and from thy heart  thankful to the gods tonight.  Remember how long thou hast been putting off these  things, and how often thou hast received an opportunity from the  gods, and yet dost not use it. Thou must now at last perceive of  what universe thou art a part, and of what administrator of the  universe thy existence is an efﬂux, and that a limit of time is ﬁxed  for thee, which if thou dost not use for clearing away the clouds  from thy mind, it will go and thou wilt go, and it will never return.  Every moment think steadily as a Roman and a man to do  what thou hast in hand with perfect and simple dignity, and  feeling of affection, and freedom, and justice; and to give thyself  relief from all other thoughts. And thou wilt give thyself relief, if  thou doest every act of thy life as if it were the last, laying aside all  carelessness and passionate aversion from the commands of  reason, and all hypocrisy, and self—love, and discontent with the  portion which has been given to thee. Thou seest how few the  things are, the which if a man lays hold of, he is able to live a life  which ﬂows in quiet, and is like the existence of the gods; for the  gods on their part will require nothing more from him who  observes these things.".split("  ")
pages=[page7,page8]
 
codes="07.10.07 07.16.02 08.19.07 08.13.06 08.06.05 07.16.02 08.14.02 08.01.04 08.09.10 07.12.04 08.08.09 08.15.04 07.16.02 07.01.03 07.33.03 08.01.04 07.23.07 07.31.11 07.27.02".split(" ")
 
 
codes=[i.split(".") for i in codes]
#page7=[i.split(" ") for i in page7]
#page8=[i.split(" ") for i in page8]
 
#print(codes,page7,page8)
 
for i in range(len(pages)):
    for j in range(len(pages[i])):
        pages[i][j]=pages[i][j].split(" ")
 
for i in range(len(codes)):
    codes[i]=[int(x) for x in codes[i]]
    print(re.sub(r'\W+', '', pages[codes[i][0]%7][codes[i][1]-1][codes[i][2]-1]))
 
