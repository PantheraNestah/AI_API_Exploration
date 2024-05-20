import json
import re

# Define the input text
input_text = """
**Technical Controls**

* **Electrostatic precipitators (ESPs):** Charged electrodes collect particulate matter from exhaust gases.
* **Fabric filters (baghouses):** Woven or felt fabric traps particulate matter from gases.
* **Scrubber systems:** Wet or dry processes that use a reagent to absorb pollutants.
* **Catalytic converters:** Reduce emissions from vehicles by converting pollutants into less harmful substances.
* **Adsorption and absorption:** Use of activated carbon or other materials to trap pollutants.

**Process Modifications**

* **Combustion modifications:** Optimizing combustion conditions to reduce emissions, such as low-NOx burners.
* **Process substitution:** Replacing polluting processes with cleaner alternatives.
* **Raw material substitution:** Using less polluting raw materials.
* **Energy efficiency:** Reducing energy consumption, which can lower emissions.
* **Waste minimization:** Reducing the amount of waste generated to minimize emissions from waste handling and disposal.

**Control Equipment**

* **Venturi scrubbers:** Use a high-pressure water spray to remove pollutants.
* **Cyclone separators:** Use centrifugal force to separate particulate matter from gases.
* **Bag filters:** Remove particulate matter from gases by filtering them through a fabric bag.
* **Thermal oxidizers:** Destroy organic pollutants by burning them at high temperatures.
* **Biofilters:** Use microorganisms to break down pollutants.

**Regulatory Measures**

* **Emission standards:** Set limits on the amount of pollutants allowed to be emitted.
* **Permitting requirements:** Regulate industrial activities to ensure compliance with emission standards.
* **Monitoring and reporting:** Require industries to monitor and report their emissions.
* **Economic incentives:** Provide tax breaks or subsidies to businesses that implement pollution prevention measures.
* **Public awareness and education:** Inform the public about the importance of air pollution prevention.

**Other Approaches**

* **Green building practices:** Designing and operating buildings to reduce energy consumption and indoor air quality.
* **Transportation alternatives:** Promoting walking, cycling, and public transportation to reduce vehicle emissions.
* **Renewable energy sources:** Switching to renewable energy sources, such as solar and wind power, to reduce reliance on fossil fuels.
* **Carbon capture and storage:** Capturing and storing carbon dioxide emissions to prevent their release into the atmosphere.
"""

def response_text_formatter(raw_text):
    sections_dict = {}
    sections = re.split(r'(\*\*.*?\*\*)\n', input_text)
    # Iterating through the sections to populate the dictionary
    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        text_block = sections[i + 1].strip()
        sections_dict[heading] = text_block
    # Formatting the text in the keys and values
    keys_list = []
    values_list = []
    new_dict = {}
    for key, value in sections_dict.items():
        new_key = key.replace("**", "")
        keys_list.append(new_key)

        new_value = value.replace("**", "")
        new_value = value.replace("*", "")
        values_list.append([new_value])

    final_dict = dict(zip(keys_list, values_list))
    return (final_dict)

print(response_text_formatter(input_text).keys())
