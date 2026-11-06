# Safety

These controllers run on low-voltage DC (5–24 V) but can switch **a lot of current**.
A K32 with every port loaded can deliver well over 100 A across its banks. At that
level, the hazards are fire from loose or undersized wiring, and the mains (AC)
side of your power supplies.

!!! danger "Mains voltage"
    - **Never connect household AC (120/230 V) to any terminal on the controller.** The
      controller only accepts DC from a power supply.
    - Have the AC side of your power supplies wired by someone qualified. Use
      grounded (3-prong) cords and close the terminal covers on the supply.
    - Unplug the AC before you touch the supply's output terminals or the controller's
      power terminals.

!!! warning "Fire prevention"
    - **Never fit a larger fuse than the one supplied**, and never bridge a fuse
      holder. The fuse protects the pixel wiring; a bigger fuse lets that wiring
      overheat.
    - Use wire rated for the current it carries (see [Power → Wire size](../hardware/power.md#wire-size)).
      Tighten every screw terminal firmly. A loose terminal heats up under load.
    - Tin or ferrule stranded wire ends. Stray strands can short to the next terminal.
    - Mount the controller in an enclosure, away from flammable material. Leave room for
      airflow, especially around the power terminals and the eFuse/fuse area.

!!! warning "Polarity and voltage"
    - Check **V+** and **G/V−** on every terminal before you power up. The power inputs
      have reverse-polarity protection, so reversed power won't damage the controller;
      that bank simply stays off. **Pixels have no such protection.** Wiring a pixel
      string backwards, or running 5 V pixels from a 12 V bank, will destroy the
      pixels.
    - Every pixel port on a bank gets the voltage of that bank's power supply. Check
      that the supply voltage matches the pixels on **every** port in the bank.
    - The **PocketScroller v3 and PocketScroller-16 accept 5 V only**. Do not connect 12 V or 24 V to them.

!!! warning "Outdoors"
    The controller is not waterproof. Outdoors, mount it in a weather-resistant enclosure
    with drip loops on every cable, and keep the power supplies in an enclosure too.
    Condensation and insects cause more failures than rain does.

!!! note "Making connections"
    Turn the power off before you plug or unplug pixel connectors, receivers or power
    terminals. Network, USB, audio and DMX cables can be connected with the power on.

!!! note "Storage"
    If you store the controller for a long time, take out the clock (RTC) coin cell.
    That keeps it from draining and leaking.
