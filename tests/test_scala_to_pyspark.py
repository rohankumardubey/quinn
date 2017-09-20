from quinn.scala_to_pyspark import ScalaToPyspark

class TestScalaToPyspark(object):

    # def test_clean_function_definition(self):
        # s = ScalaToPyspark("blah")
        # assert(s.clean_function_definition("def toArrayOfMaps(df: DataFrame) = {") == "def toArrayOfMaps(df):")

    def test_clean_args(self):
        s = ScalaToPyspark("blah")
        assert(s.clean_args("df: DataFrame") == "df")
        assert(s.clean_args("df: DataFrame, s1: String") == "df, s1")
        assert(s.clean_args("") == "")
