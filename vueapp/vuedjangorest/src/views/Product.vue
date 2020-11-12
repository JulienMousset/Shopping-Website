<template>
    <div class="product">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
            <div class="container">
                <div class="row">
                    <div v-for="product in APIData" :key="product.id" class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <div><img class="card-img-top" role="button" :src="getImgUrl(product.image)" v-bind:alt="product.image"></div>
                            <div class="card-body">
                                <h4 class=""><div class="text-secondary" role="button" href="">{{product.name}}</div></h4>
                                <p class="card-text">{{product.price}}</p>
                                <div class="d-flex justify-content-center align-items-center">
                                    <div class="btn-group">
                                        <div class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">-</div>
                                        <div class="card-text ml-2 mr-2">{{product.quantity}}</div>
                                        <div class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">+</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    export default {
        methods: {
            getImgUrl(imgName) {
                return require('.' + imgName)
            },
        },
        name: 'Product',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/product/',)
                .then(response => {
                    console.log('Post API has received data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>