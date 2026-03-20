# World Cup Text Game

A text-based soccer RPG played in the terminal. You're a star player returning from injury, subbed into the World Cup Final during overtime — one chance to score the Golden Goal and become a champion.

## Gameplay

You progress through three stages, each bringing you closer to the opponent's goal. At each stage, choose between passing, dribbling, or shooting — each with different success probabilities that create a risk/reward dynamic.

### Stages

| Stage | Location | Key Decision |
|-------|----------|-------------|
| 1 | Midfield | Safe pass (95%) vs. risky dribble (70%) |
| 2 | Attacking third | Long shot (5%) vs. pass (80%) vs. dribble (40%) |
| 3 | Penalty box | Shoot (85%) vs. pass (80%) vs. dribble (50%) — one chance, no retries |

### Features

- **Personalized narrative** — enter your name, country, and rival before kickoff
- **Procedural commentary** — randomized match narration with typewriter text effect
- **Probability-based outcomes** — every decision is a calculated gamble
- **ASCII art celebrations** — block-letter GOAL banner and champion screen on victory
- **Replayability** — retry from any stage or restart the full match

## Run

```bash
python text_game.py
```

No dependencies — just Python standard library (`random`, `time`).
