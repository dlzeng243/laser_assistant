<template>
  <div class="CSV">
      <input
        class="loadbutton_kerf"
        type="file"
        id="KerfSheet"
        aria-label="upload kerf spreadsheet"
        accept=".csv"
        @change="loadFile"
      />
      <div class="buttonholder_kerf" @click="passClickCSV">
        <span class="loadlabel_kerf">Upload Kerf Spreadsheet</span>
      </div>
  </div>
</template>

<script>
// const axios = require("axios").default;

export default {
  name: "CSV",
  methods: {
    loadFile: async function (event) {
      const csvfile = event.target.files[0];
      const csvcontent = await new Response(csvfile).text();
      console.log(csvcontent);
      console.log(JSON.stringify(csvcontent))
      this.$emit("incsv", csvcontent)
      return;
    },
    passClickCSV: function () {
      document.getElementById("KerfSheet").click();
    },
  },
};
</script>

<style scoped>
.loader_kerf {
  grid-row: 1;
  grid-column: 2/3;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 50;
  text-align: center;
  background-color: white;
}

.loadbutton_kerf {
  display: none;
}
.buttonholder_kerf {
  background: lightgrey;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
  /* box-shadow: 1px 1px 3px black; */
  padding: 20px;
  border-radius: 3px;
}
.buttonholder_kerf:hover,
.buttonholder_kerf:focus {
  background: darkgrey;
  cursor: pointer;
}

.loadlabel_kerf {
  font-family: sans-serif;
  font-size: 2rem;
}
</style>
