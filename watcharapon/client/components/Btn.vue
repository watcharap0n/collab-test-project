<template>

  <div>
    <v-dialog
        v-model="dialog"
        width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="red lighten-2"
            dark
            v-bind="attrs"
            v-on="on"
        >
          Click Me
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Add Customer
        </v-card-title>

        <v-card-text>
          <v-row style="margin-top: 10px">
            <v-col cols="6">
              <v-text-field
                  v-model="formElements.id"
                  label="ID"
                  placeholder="Input ID"
                  solo
              ></v-text-field>
            </v-col>

            <v-col cols="6">
              <v-text-field
                  v-model="formElements.name"
                  label="Name"
                  placeholder="Input Namd"
                  solo
              ></v-text-field>
            </v-col>


            <v-col cols="6">
              <v-text-field
                  v-model="formElements.age"
                  label="Age"
                  placeholder="Input Age"
                  solo
              ></v-text-field>
            </v-col>

            <v-col cols="6">
              <v-text-field
                  v-model="formElements.hobbie"
                  label="Hobbie"
                  placeholder="Input Hobbie"
                  solo
              ></v-text-field>
            </v-col>

          </v-row>


        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              text
              @click="postData"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>

</template>


<script>
export default {
  data() {
    return {
      dialog: false,
      formElements: {
        id: '',
        name: '',
        age: '',
        hobbie: ''
      }
    }
  },
  methods: {
    postData() {
      const path = 'http://127.0.0.1:8080/index';
      this.$axios.post(path, this.formElements)
          .then((res) => {
            console.log(res.data)
          })
          .catch((err) => {
            console.log(err)
          })
      this.dialog = false
    }
  }
}

</script>


