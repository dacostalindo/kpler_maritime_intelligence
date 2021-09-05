<template>
<div>
    <v-navigation-drawer
        :value="showDrawer"
        absolute
        left
        :width="400"
      >
      <v-container class="bv-example-row" grid-list>
        <!-- <v-row dense >
          <v-card ref='cards'
          class="mx-auto"
          width="360"
          max-height="130"
          outlined
          elevation="3"
          :key="product.name"
          v-for="product in products"
          >
          <v-list-item class="productTitle">
            <v-checkbox
            :label="product.name"
            :value="!product.checked"
            v-model="product.checked"
            v-bind:id="product.name"
            @change="checkAllProducts"
            ></v-checkbox>
          </v-list-item>
          <v-card-actions>
            <v-icon
            v-html="'$trash'" class="trash"
            @click="removeLayer(product)" text>Remove</v-icon>
            <v-spacer></v-spacer>
            <v-btn class="extent"
            @click="zoomToLayer(product)" text>Zoom to Extent</v-btn>
          </v-card-actions>
        </v-card>
        </v-row> -->
      </v-container>
  </v-navigation-drawer>
</div>
  
</template>

<script>
// import { mapState } from 'vuex';

export default {
  name: 'Drawer',
//   components: {
    
//   },
  props: [
    'showDrawer',
  ],
  watch: {
    group() {
      this.drawer = false;
    },
  },
};

</script>

<style>
/* .productTitle {
  word-break: normal;
  overflow-wrap: anywhere ;
}
.trash {
  justify-content: center;
  padding-left: 20px;
} */
</style>
