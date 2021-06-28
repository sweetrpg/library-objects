//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumePublisherPivot : Model {
    public static let schema = "volume_publishers"

    @ID
    public var id : UUID?

    @Parent(key: "volumeId")
    public var volume : Volume

    @Parent(key: "publisherId")
    public var publisher : Publisher

    public init() {}

    public init(id : UUID? = nil, volume : Volume, publisher : Publisher) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$publisher.id = try publisher.requireID()
    }

}
