import curses
import numpy as np
import time

class CLIOscilloscope:
    def __init__(self, signal_count=1, width=80, height=20):
        """
        Initialize the CLI oscilloscope.

        Args:
            signal_count (int): Number of signals to monitor.
            width (int): Width of the oscilloscope display (in characters).
            height (int): Height of the oscilloscope display (in characters).
        """
        self.signal_count = signal_count
        self.width = width
        self.height = height
        self.data = np.zeros((signal_count, width))
        self.middle_line = height // 2  # Middle of the terminal height

    def update_signals(self, new_signals):
        """
        Update the oscilloscope with new signal values.

        Args:
            new_signals (list): List of new signal values.
        """
        if len(new_signals) != self.signal_count:
            raise ValueError(f"Expected {self.signal_count} signals, got {len(new_signals)}")
        self.data = np.roll(self.data, -1, axis=1)
        for i, signal in enumerate(new_signals):
            self.data[i, -1] = signal

    def normalize_signals(self):
        """
        Normalize signals to fit the oscilloscope height around the zero line.
        """
        min_val = np.min(self.data)
        max_val = np.max(self.data)
        range_val = max_val - min_val
        if range_val == 0:
            range_val = 1
        normalized = ((self.data - min_val) / range_val * (self.height - 1)).astype(int)
        return normalized - (self.height // 2)

    def draw(self, screen):
        """
        Draw the oscilloscope on the terminal.

        Args:
            screen: curses screen object.
        """
        screen.clear()
        normalized_data = self.normalize_signals()
        for i in range(self.signal_count):
            for x in range(self.width):
                y = self.middle_line - normalized_data[i, x]
                if 0 <= y < self.height:
                    screen.addch(y, x, '*')
        screen.refresh()

def main(screen):
    oscilloscope = CLIOscilloscope(signal_count=2, width=100, height=60)

    t = 0.0
    while True:
        # Generate example signals
        signal1 = np.sin(2 * np.pi * 0.1 * t)  # Sine wave
        signal2 = np.cos(2 * np.pi * 0.1 * t)  # Cosine wave
        oscilloscope.update_signals([signal1, signal2])
        oscilloscope.draw(screen)
        t += 0.1
        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)