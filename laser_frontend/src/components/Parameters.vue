<template>
  <div class="params">
    <h1>metaSVG Print</h1>
    <p>
      <label for="scale">Scale factor:</label>
      <input name="scale" v-model.number="scale" type="number" step="0.1" @change="applyParams" />
    </p>

    <p>
      <label for="preset">Preset:</label>
      <select name="preset" v-model="preset" @change="applyPreset" ref="presets">
        <option disabled value>Please select one</option>
        <option value="">custom</option>
      </select>
    </p>
    <!-- <button @click="uploadcsv">Upload New</button> -->

    <div class="preset">
    <label for="notes">Notes:</label>
    <textarea name="notes" v-model="notes" @change="applyParams"></textarea>

    <!-- <p>
      <label for="material">Material:</label>
      <input name="material" v-model="material" @change="applyParams" />
    </p> -->
    
    <p>
      <label for="thickness">Thickness (mm):</label>
      <input name="thickness" v-model.number="thickness" type="number" step="0.1" @change="applyParams" />
    </p>

     <p>
      <label for="width">Sheet Width (mm):</label>
      <input name="width" v-model.number="width" type="number" step="0.1" @change="applyParams" />
    </p>

    <p>
      <label for="height">Sheet Height (mm):</label>
      <input name="height" v-model.number="height" type="number" step="0.1" @change="applyParams" />
    </p>

    <p>
      <label for="kerf">Kerf (mm):</label>
      <input name="kerf" v-model.number="kerf" type="number" step="0.01" @change="applyParams" />
    </p>

    <h2>Fits</h2>
    <table class="fits">
    <tr>
      <td>Joint</td>
      <th>C (mm)</th>
      <th>L (mm)</th>
      <th>I (mm)</th>
    </tr>
    <tr>
      <th>Box</th>
      <td><input name="box-c" v-model.number="boxC" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="box-l" v-model.number="boxL" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="box-i" v-model.number="boxI" type="number" step="0.001" @change="applyParams" /></td>
    </tr>
    <tr>
      <th>Tab</th>
      <td><input name="tab-c" v-model.number="tabC" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="tab-l" v-model.number="tabL" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="tab-i" v-model.number="tabI" type="number" step="0.001" @change="applyParams" /></td>
    </tr>
    <tr>
      <th>Slot</th>
      <td><input name="slot-c" v-model.number="slotC" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="slot-l" v-model.number="slotL" type="number" step="0.001" @change="applyParams" /></td>
      <td><input name="slot-i" v-model.number="slotI" type="number" step="0.001" @change="applyParams" /></td>
    </tr>
    </table>

    <h2>Output</h2>

    <p>
      <label for="style">Style (svg css):</label>
      <input name="style" v-model="style" @change="applyParams" />
    </p>

    </div>

      
    <button @click="downloadsvg">Download</button>
  </div>
</template>

<script>
export default {
  name: "Parameters",
  props: [ "presets" ],
  data: function () {
    return {
      scale:1.0,
      preset:"custom",
      notes:"No notes",
      //material: "wood",
      thickness: 3.0,
      width: 450.0,
      height: 300.0,
      kerf: 0.05,
      boxC:0, boxL:0, boxI:0,
      tabC:0, tabL:0, tabI:0,
      slotC:0, slotL:0, slotI:0,
      style:"stroke:#ff00ff;stroke-width:5px;"
    };
  },
  watch: {
    presets: function() {
      console.log("Got new presets.");
      this.updatePresetsOptions();
    }
  },
  mounted: function() {
    console.log("Presets as of mount: ", this.presets);
    this.updatePresetsOptions();
  },
  methods: {
    updatePresetsOptions: function() {
        //update the 'presets' dropdown based on 'presets' property
        const select = this.$refs.presets;
        //Always have "custom" as second option:
        select.innerHTML = "<option disabled value>Please select one</option><option value=\"custom\">custom</option>";
        //Create options for all presets:
        for (let preset of this.presets) {
            const option = document.createElement("option");
            option.value = preset["preset"];
            option.innerText = preset["preset"];
            select.appendChild(option);
        }
        //do the fancy thing where current preset is selected from params:
        this.applyParams();
    },
    applyPreset: function () {
      //TODO: load preset values from table if preset is changed
      console.log(`Preset changed to ${this.preset}`);
      for (let preset of this.presets) {
        if (preset.preset === this.preset) {
            this.notes = preset.notes;
            this.thickness = preset.thickness;
            this.width = preset.width;
            this.height = preset.height;
            this.kerf = preset.kerf;
            this.boxC = preset.boxC;
            this.boxL = preset.boxL;
            this.boxI = preset.boxI;
            this.tabC = preset.tabC;
            this.tabL = preset.tabL;
            this.tabI = preset.tabI;
            this.slotC = preset.slotC;
            this.slotL = preset.slotL;
            this.slotI = preset.slotI;
            this.style = preset.style;
            this.applyParams();
            break;
        }
      }
    },
    applyParams: function () {
      console.log(`TODO: update preset from params`);
      //TODO: change to "custom" preset if values don't match any existing preset
      this.$emit("update", {
        preset: this.preset,
        notes: this.notes,

        scale: this.scale,

        thickness: this.thickness,
        width: this.width,
        height: this.height,
        kerf: this.kerf,

        boxC: this.boxC, boxL: this.boxL, boxI: this.boxI,
        tabC: this.tabC, tabL: this.tabL, tabI: this.tabI,
        slotC: this.slotC, slotL: this.slotL, slotI: this.slotI,

        style:this.style
      });
      return;
    },
    downloadsvg: function () {
      this.$emit("download");
    },
   },
};
</script>

<style scoped>
.params {
  grid-area: panel;
  background-color: #d2d8de;
  margin: 10px;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
}
</style>
