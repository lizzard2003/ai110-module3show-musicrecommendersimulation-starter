# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**
Energy Mover 2.0

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.
I wanted to make an constant type of energy to songs that a person is listening to.
Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

Explain your scoring approach in simple language.
The model works by scoring each category and picking energy levels and rating the songs by high enerygy first.
Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data

Describe the dataset the model uses.
I am using dictories in this model.
Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well
It workds well in being consistent
Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

-Filter bubble : The user gets locked into the same few songs. In profile 1 Sunrise City & Gym Hero reportedly gets favored. In Profile 2 Only 1 option gets guranteed in top 5 everytime.

Profile 1 had enerygy of 0.8 meaning it had high energy and all songs have the same amount.
Profile 2 had an enerygy of 0.7 to each song and scored lower than profile 1.
Profile 3 had lower energy but achieved higher scores than profile 2.

## 7. Evaluation

How you checked whether the recommender behaved as expected.
I ran multiple test on the code to see if the outputs would change, I also blocked the mood on songs to see if there were changes to the output.

### User Profiles Tested

**Profile 1 - Pop Lover**

- Genre: pop, Mood: happy, Energy: 0.8 (high)
- Expected: Upbeat, danceable pop tracks

**Profile 2 - Rock Enthusiast**

- Genre: rock, Mood: energetic, Energy: 0.7 (high)
- Expected: High-energy rock music; limited catalog (only 1 rock song)

**Profile 3 - Jazz Chill Seeker**

- Genre: jazz, Mood: chill, Energy: 0.3 (low)
- Expected: Relaxed jazz; limited options (only 1 jazz song)

### What We Observed

**With Mood Scoring (Original)**

- All profiles got diverse top-5 results
- Genre + mood matching worked well for pop profile
- Rock & jazz profiles relied heavily on energy similarity due to limited catalog

**Without Mood Scoring (Feature Removal Test)**

- Rankings shifted significantly; energy became the primary differentiator
- "Sunrise City" appeared in top-5 for both Profile 1 and Profile 2
- Energy-based recommendations created filter bubbles within genres

### Surprises

- Limited dataset (10 songs) exposed filter bubble bias quickly
- "Sunrise City" dominated multiple profiles despite different preferences
- Removing mood feature revealed hidden energy-mood correlation in the data
- Genre imbalance (3 lofi vs 1 rock/jazz) forced minority-genre users into cross-genre recommendations

### Tests Run

- Compared top-5 results across all 3 profiles with/without mood scoring
- Analyzed song repetition across different profiles
- Tested feature removal to understand scoring component impact
- Examined data distribution for genre/energy/mood bias

---

## 8. Future Work

Ideas for how you would improve the model next.
I wold like to add more variety of songs to the model so it can have more variety.

### Additional Features or Preferences

**Currently Unused Song Features (High Impact)**

- **Danceability (0-1)**: Add to scoring if user wants dance-oriented music
  - Users could specify: "I want danceable music" vs "I prefer to listen passively"
- **Acousticness (0-1)**: Reveal hidden bias where low-energy songs are acoustic, high-energy are not
  - User preference: "I like live instruments" vs "I prefer electronic production"
- **Valence (0-1)**: Measure musical positivity/negativity independent of mood label
  - Separate from mood: low valence + high energy = aggressive music
- **Tempo/BPM**: Some users prefer specific tempos (running vs. studying)
  - User preference: "I prefer slow tempo (<90 BPM)" vs "I want fast-paced (>140 BPM)"

**User Interaction Features**

- **Listening History**: Track which recommendations users clicked/skipped
  - Allows real-time model retraining per user
- **Ratings**: Let users rate recommendations (1-5 stars) to refine future suggestions
  - Profile 2 users rating jazz lower could adjust cross-genre recommendations

**Discovery & Diversity Mechanisms**

- **Max-Per-Genre Limit**: Enforce diversity constraint
  - "Return at most 2 songs from the same genre" prevents Lofi dominance
- **Serendipity Factor**: 20-30% random/unexpected recommendations
  - Helps users break out of filter bubbles
- **Temporal Mood Variation**: Detect mood shifts over time
  - Morning = energetic pop, Evening = chill jazz

**Advanced Personalization**

- **Explicit vs. Implicit Preferences**: Allow users to say "I hate this feature"
  - "I dislike acoustic instruments" could lower acousticness score
- **Artist Diversity**: Prefer recommendations from different artists
  - Prevent "Neon Echo" appearing multiple times (currently has 2 songs)
- **Genre Exploration Mode**: Gradual exposure to unfamiliar genres
  - Rock fans get 60% rock + 40% adjacent genres (alt, indie)

---

## 9. Personal Reflection

A few sentences about your experience.
I think this project was a bit challenging because it is a balance of just trying to push the boundaries and make sure you can catch some of the edge cases.
Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
