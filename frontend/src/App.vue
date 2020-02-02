<template>
  <div id="app">
    <h1>Zürich Monthly Average Precipitation and Temperature</h1>
    <form>
      <br/>

<!--      <input type="text" v-model="formData.start"/>-->
      <label>Starting Year:</label><select v-model="formData.start">
        <option disabled value="">Please select one</option>
        <option>1864</option>
        <option>1865</option>
        <option>1866</option>
        <option>1867</option>
        <option>1868</option>
        <option>1869</option>
        <option>1870</option>
        <option>1871</option>
        <option>1872</option>
        <option>1873</option>
        <option>1874</option>
        <option>1875</option>
        <option>1876</option>
        <option>1877</option>
        <option>1878</option>
        <option>1879</option>
        <option>1880</option>
        <option>1881</option>
        <option>1882</option>
        <option>1883</option>
        <option>1884</option>
        <option>1885</option>
        <option>1886</option>
        <option>1887</option>
        <option>1888</option>
        <option>1889</option>
        <option>1890</option>
        <option>1891</option>
        <option>1892</option>
        <option>1893</option>
        <option>1894</option>
        <option>1895</option>
        <option>1896</option>
        <option>1897</option>
        <option>1898</option>
        <option>1899</option>
        <option>1900</option>
        <option>1901</option>
        <option>1902</option>
        <option>1903</option>
        <option>1904</option>
        <option>1905</option>
        <option>1906</option>
        <option>1907</option>
        <option>1908</option>
        <option>1909</option>
        <option>1910</option>
        <option>1911</option>
        <option>1912</option>
        <option>1913</option>
        <option>1914</option>
        <option>1915</option>
        <option>1916</option>
        <option>1917</option>
        <option>1918</option>
        <option>1919</option>
        <option>1920</option>
        <option>1921</option>
        <option>1922</option>
        <option>1923</option>
        <option>1924</option>
        <option>1925</option>
        <option>1926</option>
        <option>1927</option>
        <option>1928</option>
        <option>1929</option>
        <option>1930</option>
        <option>1931</option>
        <option>1932</option>
        <option>1933</option>
        <option>1934</option>
        <option>1935</option>
        <option>1936</option>
        <option>1937</option>
        <option>1938</option>
        <option>1939</option>
        <option>1940</option>
        <option>1941</option>
        <option>1942</option>
        <option>1943</option>
        <option>1944</option>
        <option>1945</option>
        <option>1946</option>
        <option>1947</option>
        <option>1948</option>
        <option>1949</option>
        <option>1950</option>
        <option>1951</option>
        <option>1952</option>
        <option>1953</option>
        <option>1954</option>
        <option>1955</option>
        <option>1956</option>
        <option>1957</option>
        <option>1958</option>
        <option>1959</option>
        <option>1960</option>
        <option>1961</option>
        <option>1962</option>
        <option>1963</option>
        <option>1964</option>
        <option>1965</option>
        <option>1966</option>
        <option>1967</option>
        <option>1968</option>
        <option>1969</option>
        <option>1970</option>
        <option>1971</option>
        <option>1972</option>
        <option>1973</option>
        <option>1974</option>
        <option>1975</option>
        <option>1976</option>
        <option>1977</option>
        <option>1978</option>
        <option>1979</option>
        <option>1980</option>
        <option>1981</option>
        <option>1982</option>
        <option>1983</option>
        <option>1984</option>
        <option>1985</option>
        <option>1986</option>
        <option>1987</option>
        <option>1988</option>
        <option>1989</option>
        <option>1990</option>
        <option>1991</option>
        <option>1992</option>
        <option>1993</option>
        <option>1994</option>
        <option>1995</option>
        <option>1996</option>
        <option>1997</option>
        <option>1998</option>
        <option>1999</option>
        <option>2000</option>
        <option>2001</option>
        <option>2002</option>
        <option>2003</option>
        <option>2004</option>
        <option>2005</option>
        <option>2006</option>
        <option>2007</option>
        <option>2008</option>
        <option>2009</option>
        <option>2010</option>
        <option>2011</option>
        <option>2012</option>
        <option>2013</option>
        <option>2014</option>
        <option>2015</option>
        <option>2016</option>
        <option>2017</option>
        <option>2018</option>
        <option>2019</option>
      </select>
      <br/>
      <br/>
      <label>Ending Year:</label>
<!--      <input type="text" v-model="formData.end"/>-->
      <select v-model="formData.end">
        <option disabled value="">Please select one</option>
        <option>1864</option>
        <option>1865</option>
        <option>1866</option>
        <option>1867</option>
        <option>1868</option>
        <option>1869</option>
        <option>1870</option>
        <option>1871</option>
        <option>1872</option>
        <option>1873</option>
        <option>1874</option>
        <option>1875</option>
        <option>1876</option>
        <option>1877</option>
        <option>1878</option>
        <option>1879</option>
        <option>1880</option>
        <option>1881</option>
        <option>1882</option>
        <option>1883</option>
        <option>1884</option>
        <option>1885</option>
        <option>1886</option>
        <option>1887</option>
        <option>1888</option>
        <option>1889</option>
        <option>1890</option>
        <option>1891</option>
        <option>1892</option>
        <option>1893</option>
        <option>1894</option>
        <option>1895</option>
        <option>1896</option>
        <option>1897</option>
        <option>1898</option>
        <option>1899</option>
        <option>1900</option>
        <option>1901</option>
        <option>1902</option>
        <option>1903</option>
        <option>1904</option>
        <option>1905</option>
        <option>1906</option>
        <option>1907</option>
        <option>1908</option>
        <option>1909</option>
        <option>1910</option>
        <option>1911</option>
        <option>1912</option>
        <option>1913</option>
        <option>1914</option>
        <option>1915</option>
        <option>1916</option>
        <option>1917</option>
        <option>1918</option>
        <option>1919</option>
        <option>1920</option>
        <option>1921</option>
        <option>1922</option>
        <option>1923</option>
        <option>1924</option>
        <option>1925</option>
        <option>1926</option>
        <option>1927</option>
        <option>1928</option>
        <option>1929</option>
        <option>1930</option>
        <option>1931</option>
        <option>1932</option>
        <option>1933</option>
        <option>1934</option>
        <option>1935</option>
        <option>1936</option>
        <option>1937</option>
        <option>1938</option>
        <option>1939</option>
        <option>1940</option>
        <option>1941</option>
        <option>1942</option>
        <option>1943</option>
        <option>1944</option>
        <option>1945</option>
        <option>1946</option>
        <option>1947</option>
        <option>1948</option>
        <option>1949</option>
        <option>1950</option>
        <option>1951</option>
        <option>1952</option>
        <option>1953</option>
        <option>1954</option>
        <option>1955</option>
        <option>1956</option>
        <option>1957</option>
        <option>1958</option>
        <option>1959</option>
        <option>1960</option>
        <option>1961</option>
        <option>1962</option>
        <option>1963</option>
        <option>1964</option>
        <option>1965</option>
        <option>1966</option>
        <option>1967</option>
        <option>1968</option>
        <option>1969</option>
        <option>1970</option>
        <option>1971</option>
        <option>1972</option>
        <option>1973</option>
        <option>1974</option>
        <option>1975</option>
        <option>1976</option>
        <option>1977</option>
        <option>1978</option>
        <option>1979</option>
        <option>1980</option>
        <option>1981</option>
        <option>1982</option>
        <option>1983</option>
        <option>1984</option>
        <option>1985</option>
        <option>1986</option>
        <option>1987</option>
        <option>1988</option>
        <option>1989</option>
        <option>1990</option>
        <option>1991</option>
        <option>1992</option>
        <option>1993</option>
        <option>1994</option>
        <option>1995</option>
        <option>1996</option>
        <option>1997</option>
        <option>1998</option>
        <option>1999</option>
        <option>2000</option>
        <option>2001</option>
        <option>2002</option>
        <option>2003</option>
        <option>2004</option>
        <option>2005</option>
        <option>2006</option>
        <option>2007</option>
        <option>2008</option>
        <option>2009</option>
        <option>2010</option>
        <option>2011</option>
        <option>2012</option>
        <option>2013</option>
        <option>2014</option>
        <option>2015</option>
        <option>2016</option>
        <option>2017</option>
        <option>2018</option>
        <option>2019</option>
      </select>
      <br/>
      <button type="submit">Submit</button>

<!--      <select v-model="selected">-->
<!--        <option disabled value="">Please select one</option>-->
<!--        <option>1864</option>-->
<!--        <option>1865</option>-->
<!--      </select>-->
<!--      <span>Selected: {{ formData.selected}}</span>-->

<!--      <select v-for="year in years"-->
<!--              v-model="year.selectedOption">-->
<!--        <option v-for="year in years.options":value="year">-->
<!--        </option>-->
<!--      </select>-->
    </form>

    <br/>
<!--    <h1>Records</h1>-->


<!--<table>-->

<!--<thead>-->

<!--<tr>-->


<!--<th>Year</th>-->
<!--<th>Month</th>-->
<!--<th>Temperature</th>-->
<!--<th>Precipitation</th>-->

<!--</tr>-->
<!--</thead>-->
<!--<tbody>-->
<!--<tr v-for="year in years">-->

<!--<th>{ { year.year } }</th>-->

<!--<th>{ { year.month } }</th>-->

<!--<td>{ { year.temperature } }</td>-->

<!--<td>{ { year.precipitation } } </td>-->

<!--</tr>-->

<!--</tbody>-->
<!--</table>-->
<div>
</div>
</div>



</template>

<script>
//  const years = [
//   {
//     options:[1864, 1865, 1866],
//     selectedOption: 1864
//   }
// ]



  import api from './api/index'
import {APIService} from "./APIService";


const API_URL = 'http://127.0.0.1:7000';
const apiService = new APIService();

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to TempPrecip',
      years: [],
      numberOfYears:0,
      formData: {
        start: '',
        end: '',
        //years
       // selected: ''
      }

    }
  },
  methods: {
    getAllRecords: function () {
      apiService.getAllRecords().then((data) => {

        this.years = data.data;
        this.numberOfYears = data.count;
      })
    },
    },

  mounted: function () {
    this.getAllRecords();
   },
   }
    // submitYears ()
    //   {
    //   api.fetchData('get', null, this.formData).then(res => {
    //       this.msg = 'Saved'
    //     }).catch((e) => {
    //       this.msg = e.response
    //   })
  //       }
  //   }
  // }

</script>

<style lang="scss">


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 60%;
  margin: 0 auto;
  text-align: left;
}

h1, h2 {
  font-weight: bold;
  font-size: 2.4rem;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
  input{
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 2px solid #ddd;
    border-radious: 4px;
    max-width: 200px;
  }

  label {
    margin-top: 15px;
    margin-bottom: 5px;
    display: block;
    font-size: 1.8rem;
  }

  button {
    margin-top: 30px;
    background: mediumaquamarine;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
    font-size: 1.8rem;

  }

  select {
    font-size: 1.1rem;
  }
</style>
