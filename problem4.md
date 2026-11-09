You get a list of daily P&L values, which can be positive, negative, or zero, and an integer target. Count how many contiguous stretches of days have a total P&L of exactly target.

count_streaks([1, 2, 3, -3, 3], 3)  # → 5

The five stretches are [1, 2], [3], [1, 2, 3, -3], [3, -3, 3], and the last [3].

Constraints

1 ≤ len(pnl) ≤ 2 × 10^5
-10^4 ≤ pnl[i] ≤ 10^4
-10^9 ≤ target ≤ 10^9

Rules, same as a real test:

Start a 25-minute timer.
Write count_streaks(pnl, target) and run it yourself, with your own asserts for edge cases.
Push it as problem5.py and tell me how long it took.
I’ll reply with only a score, e.g. “9/12 hidden tests passed”. You can resubmit while there’s time left.
When time’s up, we review the failing cases together.

Hidden tests include large inputs, so check the constraints before you choose an approach. Your timer starts now.