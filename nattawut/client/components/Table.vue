<template>

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
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>001</td>
          <td>Kane</td>
          <td>24</td>
          <td>Game</td>
        </tr>
      </tbody>

    </template>
  </v-simple-table>

</template>

<script>
export default {}

</script>

<style scoped></style>

