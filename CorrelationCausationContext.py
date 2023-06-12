import streamlit as st
from streamlit_extras.colored_header import colored_header
from PIL import Image

st.title('Statistical Storytelling:📖')
colored_header(
    label="Correlation, Causation, and Context",
    description="10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com",
    color_name="red-70",
)

head_image = Image.open('JUNE-DL-img1.png')
st.image(head_image)

''
'Your colleague is looking to measure productivity throughout the Firm. After doing some research, they note that the number of cats adopted by employees has increased as number of hours logged at the computer has increased. '
'“Naturally,” your colleague concludes, “having cats causes employees to spend more time at their computer. If we want to increase productivity, we should encourage employees to adopt more cats.” '
'Let’s explore this claim. We’ll start with the first piece: the relationship between number of cats and number of hours logged. The relationship your colleague has noted is a :red[__correlation__]. '
'What is correlation? Correlation describes the __linear relationship__ between two variables. This relationship is described by __strength and direction__ (positive or negative). '
''

definition_image = Image.open('JUNE-DL-img2.png')
st.image(definition_image)

''
'A __positive relationship__ between two variables means that as __one increases, the other increases__. For example, the number of cats I have and the amount of cat food I purchase. Conversely, a __negative relationship__ means that as __one variable increases, the other decreases__. For example, the number of cats in my household, and the number of fragile items I leave on my counters.  '
''
correl_image = Image.open('JUNE-DL-img3.png')
st.image(correl_image)
''
st.expander('Expander')
with st.expander('Deeper Dive: How do I interpret correlation?'):
    st.write('Correlation statements are often accompanied by a number called the correlation coefficient. Correlation coefficients range from 0-1 and describe the strength of a correlation. Generally, the closer the number to +/-1, the stronger the relationship between variables. Remember, correlation statements can be positive or negative. The closer the number to 0, the weaker the relationship. For instance, 0.31 would be a weak correlation. But -.89 would be a strong correlation.')

st.expander('Expander')
with st.expander(':red[__Check Your Understanding__] ✍️'):
    'Use the image below to answer the following questions.'
    direction_image = Image.open('correlationdirectionquiz.png')
    st.image(direction_image) 
    ''
    '__Question 1.__   Which of the above images depicts a __strong positive__ correlation?'       
    if st.checkbox("A"):
            st.write('That’s correct! Keep going!')
    if st.checkbox("B"):
            st.write('Not quite – try again.')
    if st.checkbox("C"):
            st.write('Not quite – try again.')
    if st.checkbox("D"):
            st.write('Not quite – try again.')
    '__Question 2.__   Which of the above images depicts a __strong negative__ correlation?'
    if st.checkbox("a"):
            st.write('Not quite – try again.')
    if st.checkbox("b"):
            st.write('Not quite – try again.')
    if st.checkbox("c"):
            st.write('Not quite – try again.')
    if st.checkbox("d"):
            st.write('That’s correct! Keep going!')
''
'__Congratulations! You’ve identified strength and direction of variables.__'
st.text('🌟Learning outcome 1: Strength and direction in correlation 🌟')
''
'Now that you’re a correlation pro, you look at the data your colleague pulled. Sure enough, it appears that your colleague was correct in noting the strong correlation between cat adoption and hours worked. But something still feels off to you. You think back to your data literacy module and remember... '
st.subheader('⚠️There\'''s a twist!⚠️')
'Just because there is a correlation between two variables does not mean that there is a cause-and-effect relationship between the two variables. In other words: correlation does not imply causation.  '
''
cause_image = Image.open('JUNE-DL-img4.png')
st.image(cause_image)
''
'You’ve likely heard this statement before, but what does this ___really___ mean?'
'Simply, it means that __a change in one variable _does not necessarily_ lead to a change in the other.__ Rather, the two variables might be explained by another element.'
'Let’s go back to our original example. What’s going on here? Should the Firm encourage employees to adopt cats to increase productivity? Sadly...no. (Or at least, not for that reason.) There is likely another underlying cause that could explain the increase in both variables – such as more remote work opportunities.'
''
st.subheader('Always look at the surrounding context and question what other factors might influence the result.')
''
'Oftentimes it is clear that there is no cause-and-effect relationship between two variables. But other times, separating correlation from causation can be tricky. You might have identified right away that it didn’t quite make sense to be looking at pet ownership. So let’s ✍️ check your understanding of causation using another example... '
'What if your colleague had instead brought you a report showing a correlation between hours worked and number of meetings scheduled per day? You notice that these variables are positively correlated. ___Which answer best describes how you can interpret this correlation?___ '
''
'__1.__ As number of meetings increases, hours worked increases.'
'__2.__ As number of meetings increases, hours worked decreases.'
'__3.__ An increase in number of meetings causes hours worked to increase. '
'__4.__ An increase in hours worked leads to an increase in number of meetings. '
''
st.expander('Expander')
with st.expander('Show me the answers!'):
    st.write('__1.__ Correct! This is the correct way to describe a correlation without assuming causation. It would also be true to say that as X decreases, Y decreases. Positive correlations will match direction.')
    st.write('__2.__ Partially incorrect! This is not a cause-and-effect statement, but this is incorrect because it would describe a negative relationship.')
    st.write(    '__3.__ Incorrect! This assumes a causal relationship. We do not have enough information based on correlation alone to explain the increase in Y.')
    st.write(    '__4.__ Incorrect! This assumes a causal relationship. Like #3, we do not have enough information based on correlation alone to explain the increase in Y. It looks like a correlation statement upon first glance, but be careful of any causal language.')
'It makes sense that if you have more meetings, you work longer days. Perhaps you have even argued that having more meetings causes you to work longer. But there may be other factors at play to explain this correlation: perhaps you are accommodating different time zones, perhaps there is a deadline you are moving toward, perhaps you are just a hard worker. '
'Regardless of the reason, we need to __dig deeper into the surrounding context__ to fully understand why there seems to be a relationship between meeting volume and hours worked.  '
''
st.expander('Expander')
with st.expander('An example of the importance of context'):
    st.write(
        'Take, for example, this webpage <https://tylervigen.com/spurious-correlations>. This page shows examples of real relationships between data that appear strikingly similar, but are unrelated – such as per capita mozzarella consumption, and civil engineering doctorates awarded. ')
'Remember, correlation is just a linear relationship between data, not a causal one. Any time you see causal language describing a correlation, proceed with caution! '
''
'__Congratulations! You’ve learned the difference between correlation and causation.__'
''
redflag_image = Image.open('JUNE-DL-img5.png')
st.image(redflag_image)
''
st.text('🌟 Learning outcome 2: Before making inferences from your data, stop and consider \n other factors that may influence the result. 🌟')
''
'Thank you for reading along! As always, the Data Governance team is here to support you on your data literacy journey. If you have any questions, please reach out to us at DataGovernance@perkinscoie.com. Happy June! '
''
if st.button('🌟You are a data star!🌟'):
    from streamlit_extras.let_it_rain import rain    
    rain(
        emoji="🌟",
        font_size=54,
        falling_speed=5,
        animation_length="short",
        )
    
'Have feedback on the new format? Please let us know via email or by clicking feedback at the end of the intiial communication. '
