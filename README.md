# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

My design will have more weight on the energy of the song more then the mood value. This will not only give the person songs with the same energy tune but it will keep them at the same mood. In the real world I believe the songs are picked by what artist the person likes and keeps on playing the artist similar to that artist.

The plan is to load the songs,
read the CVS file, make a dictionary and store the songs there.
Define the users preferences
Then we will score the song.
Then we will create an explanation to the score.
The songs then get scored and get ranked from highest to lowest.
We then finally return the songs and you can pick the amount of songs you want a top for.

A bias that might happen is it would pick the songs that are more important.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    The song object will use the following features : artist, genre, mood, energy, tempo bpm
- What information does your `UserProfile` store

The UserProfile will store :
favorite_genre
favorite_mood
target_energy

- How does your `Recommender` compute a score for each song
  It will score each song by energy and mood.
- How do you choose which songs to recommend
  I will choose the song by weighted score

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```text
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
Top recommendations:

Title: Sunrise City
Score: 6.46
Reasons: genre match (+2.0); mood match (+2.5); energy match to user preference (+1.96); user likes genre pop; user likes mood happy; user target energy is 0.8
--------------------------------------------------
Title: Rooftop Lights
Score: 4.42
Reasons: mood match (+2.5); energy match to user preference (+1.92); user likes mood happy; user target energy is 0.8
--------------------------------------------------
Title: Gym Hero
Score: 3.74
Reasons: genre match (+2.0); energy match to user preference (+1.74); user likes genre pop; user target energy is 0.8
--------------------------------------------------
Title: Night Drive Loop
Score: 1.90
Reasons: energy match to user preference (+1.90); user target energy is 0.8
--------------------------------------------------
Title: Storm Runner
Score: 1.78
Reasons: energy match to user preference (+1.78); user target energy is 0.8
--------------------------------------------------
Title: Midnight Coding
Score: 1.24
Reasons: energy match to user preference (+1.24); user target energy is 0.8
--------------------------------------------------
Title: Focus Flow
Score: 1.20
Reasons: energy match to user preference (+1.20); user target energy is 0.8
--------------------------------------------------
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
  I learned about how Spotify works and how we can make a model have specific rules to pick specific songs. For instance in my case I wanted the user to keep a consistent flow of energy so I made that be the main focus. Because of this I also wanted the mood of the songs picked to be the second rule.
  There were limitions to this project that I would like to expand on . The first being adding a bigger library to the list of songs and incorporatring more features that the user might want.

## Stress Test with Diverse Profiles

Profile 1: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}

Title: Sunrise City
Score: 6.46
Reasons: genre match (+2.0); mood match (+2.5); energy match to user preference (+1.96); user likes genre pop; user likes mood happy; user target energy is 0.8

---

Title: Rooftop Lights
Score: 4.42
Reasons: mood match (+2.5); energy match to user preference (+1.92); user likes mood happy; user target energy is 0.8

---

Title: Gym Hero
Score: 3.74
Reasons: genre match (+2.0); energy match to user preference (+1.74); user likes genre pop; user target energy is 0.8

---

Title: Night Drive Loop
Score: 1.90
Reasons: energy match to user preference (+1.90); user target energy is 0.8

---

Title: Storm Runner
Score: 1.78
Reasons: energy match to user preference (+1.78); user target energy is 0.8

---

Profile 2: {'genre': 'rock', 'mood': 'energetic', 'energy': 0.7}

Title: Storm Runner
Score: 3.58
Reasons: genre match (+2.0); energy match to user preference (+1.58); user likes genre rock; user target energy is 0.7

---

Title: Night Drive Loop
Score: 1.90
Reasons: energy match to user preference (+1.90); user target energy is 0.7

---

Title: Rooftop Lights
Score: 1.88
Reasons: energy match to user preference (+1.88); user target energy is 0.7

---

Title: Sunrise City
Score: 1.76
Reasons: energy match to user preference (+1.76); user target energy is 0.7

---

Title: Gym Hero
Score: 1.54
Reasons: energy match to user preference (+1.54); user target energy is 0.7

---

Profile 3: {'genre': 'jazz', 'mood': 'chill', 'energy': 0.3}

Title: Spacewalk Thoughts
Score: 4.46
Reasons: mood match (+2.5); energy match to user preference (+1.96); user likes mood chill; user target energy is 0.3

---

Title: Library Rain
Score: 4.40
Reasons: mood match (+2.5); energy match to user preference (+1.90); user likes mood chill; user target energy is 0.3

---

Title: Midnight Coding
Score: 4.26
Reasons: mood match (+2.5); energy match to user preference (+1.76); user likes mood chill; user target energy is 0.3

---

Title: Coffee Shop Stories
Score: 3.86
Reasons: genre match (+2.0); energy match to user preference (+1.86); user likes genre jazz; user target energy is 0.3

---

Title: Focus Flow
Score: 1.80
Reasons: energy match to user preference (+1.80); user target energy is 0.3

---
