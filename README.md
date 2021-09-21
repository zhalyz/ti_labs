curl --location --request GET 'http://downloads.scylladb.com.s3.amazonaws.com/?delimiter=/&prefix=downloads/scylla/relocatable/scylladb-4.4/'
OUTPUT_DIR='/root/scylladb/'
if [[ -d $OUTPUT_DIR ]]; then
  strings=$(cat test.xml |
            sed 's/<Contents>/\n/g'
           )
  site='http://downloads.scylladb.com/'
  for string in $strings
  do
    str=$(echo -e $string |
          grep '<Key>' |
          awk -F '</Key' '{print $1}' |
          sed 's/<Key>//g')
    tag=$(echo -e $string |
          grep '<Key>' |
          awk -F '<ETag>' '{print $2}' |
          awk -F '</ETag>' '{print $1}' |
          sed 's/&quot;//g'
         )
    filname=$(echo $str |
              awk -F '/' '{print $NF}'
             )
    if [ ! -f $OUTPUT_DIR$filname ] && [ ! -z $filname ]; then
      curl $site$str -o $(echo $str |
                          awk -F '/' '{print $NF}'
                         )
    fi
  done
  else
    echo $OUTPUT_DIR' is not exists!'
fi
