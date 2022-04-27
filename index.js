// what if I comment here?
module.exports = async function getSnakeRiverFlows() {
  const uri =
    "http://waterservices.usgs.gov/nwis/iv/?site=13022500&format=json";

  const xhr = new XMLHttpRequest();

  xhr.open("GET", uri);

  xhr.onload = () => {
    if (xhr.status === 200) {
      data = JSON.parse(xhr.responseText);
      console.log(data);
      return data;
    } else {
      console.log("Something went wrong!!");
    }
  };
};
