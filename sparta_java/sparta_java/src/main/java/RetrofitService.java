import jdk.nashorn.internal.objects.annotations.Getter;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface RetrofitService {
    @GET("/api/users/")
    Call<Object> getUsers(@Query("page") int page);

}
