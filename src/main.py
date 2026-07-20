from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_profiles = [
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        {"genre": "rock", "mood": "energetic", "energy": 0.7},
        {"genre": "jazz", "mood": "chill", "energy": 0.3},
    ]

    for index, user_prefs in enumerate(user_profiles, start=1):
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nProfile {index}: {user_prefs}\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"Title: {song['title']}")
            print(f"Score: {score:.2f}")
            print(f"Reasons: {explanation}")
            print("-" * 50)


if __name__ == "__main__":
    main()
