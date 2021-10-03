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

    <v-simple-table>
      <template v-slot:default>
        <thead>
        <tr>
          <th class="text-center">
            ID
          </th>
          <th class="text-center">
            Name
          </th>
          <th class="text-center">
            Age
          </th>
          <th class="text-center">
            Hobbies
          </th>
          <th class="text-center">
            actions
          </th>
        </tr>
        </thead>

        <tbody>
        <tr
            v-for="(val, i) in transaction" :key="i"
        >

          <td> {{ val.id }}</td>
          <td> {{ val.name }}</td>
          <td> {{ val.age }}</td>
          <td> {{ val.hobbies }}</td>
          <td>
            <v-btn color="info" dark>Edit</v-btn>
          </td>
        </tr>
        </tbody>

      </template>
    </v-simple-table>
  </div>
</template>

<script>

export default {
  data() {
    return {
      dialog: false,
      transaction: [],
      formElements: {
        id: '',
        name: '',
        age: '',
        hobbie: ''
      }
    }
  },
  created() {
    this.initialized();
  },
  methods: {
    initialized() {
      const path = 'http://127.0.0.1:8080/index';
      this.$axios.get(path)
          .then((res) => {
            this.transaction = res.data
            console.log(res.data);
          })
          .catch((err) => {
            console.error(err);
          })
    },
    postData() {
      const path = 'http://127.0.0.1:8080/index';
      this.$axios.post(path, this.formElements)
          .then((res) => {
            this.transaction.push(this.formElements)
            this.formElements = {}
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

<style scoped></style>

