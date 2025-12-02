from gtts import gTTS

# Function to generate speech and save as MP3
def text_to_speech(text, filename="output.mp3"):
    try:
        # Create the gTTS object for text-to-speech conversion
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save the generated speech to an MP3 file
        tts.save(filename)
        print(f"Speech saved to {filename}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
text = '''
Hello and welcome!

Today, let’s discuss one of the most pressing issues our world faces—poverty. It is a challenge that affects millions across the globe, cutting across borders, communities, and generations. Poverty is not just the lack of money; it is the lack of opportunity, dignity, and access to basic human rights like education, food, shelter, and healthcare.

Globally, over 700 million people live on less than $2.15 a day, according to the World Bank. That means nearly 10% of the world’s population struggles to meet their most basic needs. Poverty traps people in cycles of deprivation, where the absence of opportunities limits their ability to improve their lives and their futures.

Now, let’s bring this closer to home—to India, one of the most diverse and populous nations in the world. India has made great strides in reducing poverty over the decades, but it still remains one of the biggest challenges our country faces.

Poverty in India: A Closer Look
Did you know that India has the single largest concentration of poor people in the world? And every fifth person in India lives below the poverty line. This means that millions of people in our country face hunger, homelessness, and a lack of access to education and healthcare.

Poverty in India has impacted several communities disproportionately. Let’s break it down:

Rural Areas:
Rural poverty remains widespread, with families struggling to make ends meet. Farmers, laborers, and small-scale workers often face seasonal unemployment and inadequate incomes. Many live in areas where access to clean water, electricity, and healthcare is still a distant dream.

Tribal Communities:
Tribal populations, especially in states like Chhattisgarh, Jharkhand, Odisha, and Madhya Pradesh, are among the most vulnerable. Displacement due to mining, deforestation, and industrial projects has uprooted many tribal families from their lands, leaving them with little to survive on.

Urban Slums:
Poverty isn’t just a rural problem. In urban areas, millions live in overcrowded slums with poor sanitation and no reliable source of clean water or electricity. Cities like Mumbai, Delhi, and Kolkata are home to some of the largest slums in the world, where people live in precarious conditions despite being surrounded by wealth and development.

Marginalized Communities:
Groups like Scheduled Tribes, Scheduled Castes, and Other Backward Classes face systemic inequalities that limit their opportunities. Lack of access to quality education and discrimination in job markets often perpetuate cycles of poverty for these groups.

The Impact of Poverty
The effects of poverty are devastating and far-reaching. It impacts not just individuals but entire communities and future generations. Here’s how:

Education: Poverty forces millions of children to drop out of school to work and support their families. Without education, they are unable to break free from the cycle of poverty.
Health: Poor families often cannot afford healthcare, leading to high rates of malnutrition, infant mortality, and preventable diseases.
Social Inequality: Poverty deepens the gap between the rich and the poor, creating divisions in society.
Economic Growth: A nation cannot progress if a significant part of its population is struggling to meet basic needs. Poverty stunts overall development.
Steps to Reduce Poverty in India
Despite these challenges, there is hope. India has already made significant progress, and with collective effort, we can do more. Here are some of the key strategies to combat poverty:

Promote Education:
Education is the foundation for breaking the cycle of poverty. Programs like Sarva Shiksha Abhiyan and Mid-Day Meal Scheme have encouraged children to stay in school. More focus on improving the quality of education is needed to equip children with the skills they need for better futures.

Skill Development and Employment:
Unemployment is a major contributor to poverty. Initiatives like Skill India and Startup India can train young people in relevant skills, helping them find jobs or start businesses. Employment guarantee programs like MGNREGA have also provided income security to millions of rural households.

Support for Women and Marginalized Groups:
Empowering women through programs like Self-Help Groups (SHGs) and financial literacy initiatives can uplift entire families. Similarly, providing targeted support to marginalized communities can help them overcome systemic barriers.

Affordable Housing and Urban Development:
Schemes like Pradhan Mantri Awas Yojana aim to provide affordable housing to the poor. Better urban planning and investment in slum rehabilitation projects are essential to improving living conditions in cities.

Access to Healthcare:
Programs like Ayushman Bharat, which provides free healthcare to low-income families, are crucial in reducing the financial burden of illness. Ensuring affordable medicines and hospital care can prevent families from falling deeper into poverty.

Sustainable Agriculture:
Supporting small-scale farmers with better technology, fair prices for their produce, and access to markets can reduce rural poverty.

Social Security and Subsidies:
Direct Benefit Transfers (DBT) and subsidies for food, fuel, and fertilizers help ease the financial burden on the poor. Strengthening these programs can ensure that resources reach those who need them most.

Conclusion
Poverty is more than just an economic problem—it is a human problem. It limits people’s potential, deprives them of their dignity, and keeps entire communities trapped in a cycle of struggle. But it is not an unsolvable problem.

India has made great progress in reducing poverty, but there is still a long way to go. By focusing on education, healthcare, skill development, and empowering communities, we can create a society where everyone has the opportunity to thrive.

The fight against poverty is not just the government’s responsibility. It’s a collective effort that requires each of us to contribute—whether it’s by spreading awareness, volunteering, or supporting sustainable development initiatives.

Together, we can break the cycle of poverty and build a future where every person can live with dignity and hope.

Thank you for listening!
'''
text_to_speech(text, filename="girl_speech.mp3")
