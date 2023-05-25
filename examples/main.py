import fastvector


def main() -> None:
    vec1 = fastvector.Vector2D(-1, 1)
    vec2 = fastvector.Vector2D(2.5, -2.5)
    print(vec1 - vec2)


if __name__ == "__main__":
    main()
