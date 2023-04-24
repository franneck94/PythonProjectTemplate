import fastvector


def main() -> None:
    V1 = fastvector.Vector2D(-1, 1)
    V2 = fastvector.Vector2D(2.5, -2.5)
    print(V1 - V2)


if __name__ == "__main__":
    main()
