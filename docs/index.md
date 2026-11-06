---
hide:
  - navigation
---

<p align="center" markdown>
![Kulp Lights](assets/kulp-lights-logo.png){ width="420" .kulp-hero }
</p>

# Kulp Lights Controller Manual

This manual covers the **hardware** of the Kulp Lights controllers.

## PocketBeagle 2 controllers

<div class="grid cards" markdown>

-   **K8-Pro · K8-Max**

    ---

    8 local pixel ports + 4 differential ports (16 strings).

    [:octicons-arrow-right-24: K8-Pro](boards/k8-pro.md) · [K8-Max](boards/k8-max.md)

-   **K8-PB · K4-PB · K40D-PB**

    ---

    Compact: 8 or 4 local pixel ports, or 40 strings on 10 differential ports (K40D-PB).

    [:octicons-arrow-right-24: K8-PB](boards/k8-pb.md) · [K4-PB](boards/k4-pb.md) · [K40D-PB](boards/k40d-pb.md)

-   **K16 · K16-Pro · K16-Max**

    ---

    16 local pixel ports + 4 or 8 differential ports.

    [:octicons-arrow-right-24: K16](boards/k16.md) · [K16-Pro](boards/k16-pro.md) · [K16-Max](boards/k16-max.md)

-   **K32 · K32-Pro · K32-Max**

    ---

    32 local pixel ports + 4 or 8 differential ports.

    [:octicons-arrow-right-24: K32](boards/k32.md) · [K32-Pro](boards/k32-pro.md) · [K32-Max](boards/k32-max.md)

-   **PocketScroller v2 · v3 · -16**

    ---

    6, 8 or 16 HUB75 outputs for LED panel matrices.

    [:octicons-arrow-right-24: PocketScroller v2](boards/pocketscroller-v2.md) · [v3](boards/pocketscroller-v3.md) · [PocketScroller-16](boards/pocketscroller-16.md)

</div>

## BeagleBone Black controllers

<div class="grid cards" markdown>

-   **K8-B · K8-B-Scroller**

    ---

    8 fused pixel ports + differential ports; the K8-B-Scroller adds 3 HUB75 panel outputs.

    [:octicons-arrow-right-24: K8-B](boards/k8-b.md) · [K8-B-Scroller](boards/k8-b-scroller.md)

-   **K64D-B · K128D-B**

    ---

    64 or 128 strings on 16 or 32 differential ports, with audio and two DMX/LOR outputs.

    [:octicons-arrow-right-24: K64D-B](boards/k64d-b.md) · [K128D-B](boards/k128d-b.md)

-   **OctoPlus**

    ---

    8 HUB75 outputs for LED panel matrices.

    [:octicons-arrow-right-24: OctoPlus](boards/octoplus.md)

</div>

## Raspberry Pi controllers

<div class="grid cards" markdown>

-   **K8-Pi**

    ---

    8 eFused pixel ports + 3 differential ports and an expansion port: 36 strings.

    [:octicons-arrow-right-24: K8-Pi](boards/k8-pi.md)

-   **K2-Pi-Servo · K2-Pi0**

    ---

    2 eFused pixel ports, plus 16 servo outputs (K2-Pi-Servo) or on a Pi Zero (K2-Pi0).

    [:octicons-arrow-right-24: K2-Pi-Servo](boards/k2-pi-servo.md) · [K2-Pi0](boards/k2-pi0.md)

</div>

Every one of these boards is a *cape* (or *hat*) for a **PocketBeagle 2**, a **BeagleBone Black**
or a **Raspberry Pi** and runs **FPP (Falcon Player)**. FPP is the software that plays your show, and it has its own
manual at **[manual.falconplayer.com](https://manual.falconplayer.com)**. This manual
doesn't repeat that one. It covers what the FPP manual can't:

- **[Power](hardware/power.md)**: wiring power supplies, banks, fuses and eFuses.
- **[Pixel outputs](hardware/pixel-outputs.md)** and **[differential ports](hardware/differential.md)**: wiring pixels and receivers.
- **[Controls & display](hardware/controls.md)**: the buttons, the OLED menus and the status LEDs.
- **Board pages**: one per controller, with specifications, connector maps and dimensions.
- **[Troubleshooting](troubleshooting.md)** for hardware problems.

!!! danger "Read the [Safety](getting-started/safety.md) page before you connect a power supply."

## Where to start

1. Not sure which board you have? See **[Which board do I have?](getting-started/which-board.md)**
2. Setting one up for the first time? Follow the **[Quick start](getting-started/quick-start.md)** checklist.
3. Something not working? Go to **[Troubleshooting](troubleshooting.md)**.

!!! tip "Printing or saving a PDF"
    The **[Print / PDF](print_page/)** page puts the whole manual on one page.
    Use your browser's *Print → Save as PDF* to save it as a PDF.

---

<small>Found a mistake or something missing? Email **support@kulplights.com** or use
the :material-file-edit-outline: edit link at the top of any page.</small>
