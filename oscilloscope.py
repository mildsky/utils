import matplotlib.pyplot as plt
import numpy as np

class Oscilloscope:
    def __init__(self, signal_count, time_horizon):
        """
        Initialize the oscilloscope.
        
        Args:
            signal_count (int): Number of signals to monitor.
            time_horizon (int): Length of the time horizon to display (number of samples).
        """
        self.signal_count = signal_count
        self.time_horizon = time_horizon
        self.data = np.zeros((signal_count, time_horizon))
        self.time = np.arange(time_horizon)
        
        # Setup the plot
        self.fig, self.ax = plt.subplots()
        self.lines = [
            self.ax.plot(self.time, self.data[i], label=f"Signal {i+1}")[0]
            for i in range(signal_count)
        ]
        self.ax.set_ylim(-1.5, 1.5)  # Default signal range; adjust as needed
        self.ax.set_xlim(0, time_horizon)
        self.ax.legend(loc="upper right")
        self.ax.set_title("Oscilloscope")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amplitude")
        plt.ion()  # Enable interactive mode
        plt.show()

    def draw(self, signals):
        """
        Update the oscilloscope with new signal values.
        
        Args:
            signals (list): List of signal values to update.
        """
        if len(signals) != self.signal_count:
            raise ValueError(f"Expected {self.signal_count} signals, got {len(signals)}")
        
        # Shift data and append new values
        self.data = np.roll(self.data, -1, axis=1)
        self.data[:, -1] = signals
        
        # Update plot lines
        for i, line in enumerate(self.lines):
            line.set_ydata(self.data[i])
        
        # Redraw the figure
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == "__main__":
    import time
    scope = Oscilloscope(3, 100)  # 3 signals, 100 time horizon

    x, y, z = 0.0, 0.0, 0.0  # Initialize signals
    t = 0.0

    while True:
        # Simulate some signals
        x = np.sin(2 * np.pi * 0.1 * t)  # Sine wave
        y = np.cos(2 * np.pi * 0.1 * t)  # Cosine wave
        z = 0.5 * np.sin(2 * np.pi * 0.2 * t) + 0.3 * np.random.randn()  # Noisy sine wave
        
        scope.draw([x, y, z])  # Update the oscilloscope
        t += 0.1  # Increment time
        time.sleep(0.01)  # Simulate a sampling interval of 100ms